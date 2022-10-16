from django import forms 
from .models import Messages
# from email_validator import validate_email
from phonenumber_field.formfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class MessagesForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = '__all__'

        labels = {
            'name': _('Your Name (Required)'),
            'email': _('Your Email Address (Required)'),
            'subject': _('Your Subject Line'),
            'message': _('Your Message'),
        }

    phone = PhoneNumberField()
    phone.error_messages['invalid'] = _('Incorrect Phone Number Format!')
    phone.label = _('Your Phone Number')