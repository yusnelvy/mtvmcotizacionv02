from django.forms import ModelForm
from django import forms


class BaseFormMd(forms.Form):
    def as_md(self):

            "Returns this form rendered as HTML <p>s."
            return self._html_output(
                normal_row='<md-input-container%(html_class_attr)s>%(label)s %(field)s%(help_text)s</md-input-container>',
                error_row='%s',
                row_ender='</md-input-container>',
                help_text_html=' <span class="helptext">%s</span>',
                errors_on_separate_row=True)
