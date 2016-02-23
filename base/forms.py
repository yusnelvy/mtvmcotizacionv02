from django.forms import ModelForm
from django.forms.widgets import Select, CheckboxInput, Widget
from django import forms
from django.utils.html import conditional_escape, format_html, html_safe
from django.forms.utils import flatatt, to_current_timezone
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils import formats, six


class BaseFormMd(forms.Form):
    def as_md(self):

            "Returns this form rendered as HTML <p>s."
            return self._html_output(
                normal_row='<md-input-container%(html_class_attr)s>%(label)s %(field)s%(help_text)s</md-input-container>',
                error_row='%s',
                row_ender='</md-input-container>',
                help_text_html=' <span class="helptext">%s</span>',
                errors_on_separate_row=True)


class SelectMD(Select):

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<md-select{}>', flatatt(final_attrs))]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</md-select>')
        return mark_safe('\n'.join(output))

    def render_option(self, selected_choices, option_value, option_label):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html('<md-option value="{}"{} tabindex="-1">{}</md-option>',
                           option_value,
                           selected_html,
                           force_text(option_label))


def boolean_check(v):
    return not (v is False or v is None or v == '')


class Checkbox(Widget):
    def __init__(self, attrs=None, check_test=None):
        super(Checkbox, self).__init__(attrs)
        # check_test is a callable that takes a value and returns True
        # if the checkbox should be checked for that value.
        self.check_test = boolean_check if check_test is None else check_test

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        if self.check_test(value):
            final_attrs['checked'] = 'checked'
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(value)
        return format_html('<md-switch{} />', flatatt(final_attrs))

    def value_from_datadict(self, data, files, name):
        if name not in data:
            # A missing value means False because HTML form submission does not
            # send results for unselected checkboxes.
            return False
        value = data.get(name)
        # Translate true and false strings to boolean values.
        values = {'true': True, 'false': False}
        if isinstance(value, six.string_types):
            value = values.get(value.lower(), value)
        return bool(value)
