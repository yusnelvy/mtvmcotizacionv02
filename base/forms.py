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
        return format_html('<br><input{0}/><br>', flatatt(final_attrs))


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


class selectSearchMD(Select):

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select{}>', flatatt(final_attrs))]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
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
        return format_html('<option value="{}"{} tabindex="-1">{}</option>',
                           option_value,
                           selected_html,
                           force_text(option_label))

class InputFecha(Widget):
    """
    Base class for all <input> widgets (except type='checkbox' and
    type='radio', which are special).
    """
    input_type = None  # Subclasses must define this.

    def _format_value(self, value):
        if self.is_localized:
            return formats.localize_input(value)
        return value

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        return format_html('<md-datepicker{0} />', flatatt(final_attrs))


class radioSelectPlus(Select):

    def render(self, name, value, attrs=None, choices=()):
        checked1 = ''
        checked2 = ''
        checked3 = ''
        checked4 = ''
        checked5 = ''
        checked6 = ''
        checked7 = ''
        checked8 = ''
        checked9 = ''
        checked10 = ''
        if value is None:
            value = '1'

        if int(value) is 0 or int(value) >= 10:
            checked10 = 'checked="checked"'
        elif int(value) is 1:
            checked1 = 'checked="checked"'
        elif int(value) is 2:
            checked2 = 'checked="checked"'
        elif int(value) is 3:
            checked3 = 'checked="checked"'
        elif int(value) is 4:
            checked4 = 'checked="checked"'
        elif int(value) is 5:
            checked5 = 'checked="checked"'
        elif int(value) is 6:
            checked6 = 'checked="checked"'
        elif int(value) is 7:
            checked7 = 'checked="checked"'
        elif int(value) is 8:
            checked8 = 'checked="checked"'
        elif int(value) is 9:
            checked9 = 'checked="checked"'


        ul = '<ul>\
                <li>\
                    <label for="'+name+'1">\
                        <input id="'+name+'1" '+checked1+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">1\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'2">\
                        <input id="'+name+'2" '+checked2+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">2\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'3">\
                        <input id="'+name+'3" '+checked3+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">3\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'4">\
                        <input id="'+name+'4" '+checked4+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">4\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'5">\
                        <input id="'+name+'5" '+checked5+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">5\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'6">\
                        <input id="'+name+'6" '+checked6+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">6\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'7">\
                        <input id="'+name+'7" '+checked7+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">7\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'8">\
                        <input id="'+name+'8" '+checked8+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">8\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'9">\
                        <input id="'+name+'9" '+checked9+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'">9\
                    </label>\
                </li>\
                <li>\
                    <label for="'+name+'10">\
                        <input id="'+name+'10" '+checked10+' type="radio" onclick="clickRadioSelect(this);" name="'+name+'a" data-name="'+name+'"/>+\
                    </label>\
                </li>\
            </ul>'

        if value is None:
            value = '0'
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html(ul+'<input{} type="number" class="form-control hidden" value="'+str(value)+'">', flatatt(final_attrs))]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</md-select>')
        return mark_safe('\n'.join(output))
