import json

from directory_validators import enrolment as shared_validators
from directory_validators.constants import choices

from django import forms
from django.conf import settings

from enrolment import helpers, validators


class IndentedInvalidFieldsMixin:
    error_css_class = 'input-field-container has-error'


class CompanyForm(IndentedInvalidFieldsMixin, forms.Form):
    company_number = forms.CharField(
        label='Company number:',
        help_text=('This is the 8-digit number on the company certificate of '
                   'incorporation.'),
        validators=helpers.halt_validation_on_failure(
            shared_validators.company_number,
            validators.company_number,
        )
    )


class CompanyNameForm(IndentedInvalidFieldsMixin, forms.Form):
    company_name = forms.CharField(
        label='Company Name:',
        help_text=(
            'Please click next if this is your company.'
        ),
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
    )


class CompanyExportStatusForm(IndentedInvalidFieldsMixin, forms.Form):
    export_status = forms.ChoiceField(
        label=(
            'Has your company sold products or services to overseas customers?'
        ),
        choices=choices.EXPORT_STATUSES,
        validators=[shared_validators.export_status_intention]
    )


class CompanyBasicInfoForm(IndentedInvalidFieldsMixin, forms.Form):
    company_name = forms.CharField(
        help_text=(
            'You can change this from the Companies House listing to '
            'better fit your profile.'
        ),
        max_length=255,
    )
    website = forms.URLField(max_length=255)
    keywords = forms.CharField(
        label='Enter up to 10 keywords that describe your company:',
        help_text=(
            'Keywords should be separated with commas. These keywords will be '
            'used to help potential overseas buyers find your company.'
        ),
        widget=forms.Textarea,
        max_length=1000,
    )


class CompanyDescriptionForm(IndentedInvalidFieldsMixin, forms.Form):
    description = forms.CharField(
        widget=forms.Textarea,
        label='Describe your business to overseas buyers:',
        help_text='Maximum 1,000 characters.',
        max_length=1000,
    )


class CompanyLogoForm(IndentedInvalidFieldsMixin, forms.Form):
    logo = forms.FileField(
        help_text=(
            'For best results this should be a transparent PNG file of 600 x '
            '600 pixels and more than {0}MB'.format(
                int(settings.VALIDATOR_MAX_LOGO_SIZE_BYTES / 1024 / 1014)
            )
        ),
        required=False,
        validators=[shared_validators.logo_filesize]
    )


class CompanyEmailAddressForm(IndentedInvalidFieldsMixin, forms.Form):
    company_email = forms.EmailField(
        label='Email address:',
        help_text=(
            'Please enter a company email address rather than personal email '
            'address. This will not replace your username.'
        ),
        validators=[
            shared_validators.email_domain_free,
            shared_validators.email_domain_disposable,
        ]
    )
    email_confirmed = forms.EmailField(
        label='Email confirmed:',
        help_text='Please confirm your email address.',
    )

    def clean_email_confirmed(self):
        email = self.cleaned_data.get('company_email')
        confirmed = self.cleaned_data.get('email_confirmed')
        if (email and confirmed and email != confirmed):
            raise forms.ValidationError('Your emails do not match')
        return confirmed


class UserForm(IndentedInvalidFieldsMixin, forms.Form):
    mobile_number = forms.CharField(
        label='Mobile number:',
        help_text='We will use this to send you a verification code.',
    )
    mobile_confirmed = forms.CharField(
        label='Mobile number confirmed:'
    )
    terms_agreed = forms.BooleanField(
        label=(
            'Tick this box to accept the terms and conditions of the Great '
            'Trade Index.'
        )
    )
    referrer = forms.CharField(required=False, widget=forms.HiddenInput())

    def clean_mobile_confirmed(self):
        mobile = self.cleaned_data.get('mobile_number')
        confirmed = self.cleaned_data.get('mobile_confirmed')
        if (mobile and confirmed and mobile != confirmed):
            raise forms.ValidationError('Your numbers do not match')
        return confirmed


class CompanySizeForm(IndentedInvalidFieldsMixin, forms.Form):
    employees = forms.ChoiceField(
        choices=choices.EMPLOYEES,
        label='How many employees are in your company?',
        help_text=(
            'Customers may use this to judge how capable you are of '
            'fulfilling orders.'
        )
    )


class CompanyClassificationForm(IndentedInvalidFieldsMixin, forms.Form):
    sectors = forms.MultipleChoiceField(
        label='What sectors is your company interested in working in?',
        choices=choices.COMPANY_CLASSIFICATIONS,
        widget=forms.CheckboxSelectMultiple()
    )


class PhoneNumberVerificationForm(IndentedInvalidFieldsMixin, forms.Form):

    def __init__(self, *args, **kwargs):
        self.expected_sms_code = kwargs.pop('expected_sms_code')
        super().__init__(*args, **kwargs)

    sms_code = forms.CharField(
        label='Enter the code from the text message we sent you:',
        help_text=(
            'We have sent you an SMS text message to your mobile phone '
            'containing an six digit code which you’ll need to enter on the '
            'verification page to complete your Export Connect account.'
        ),
    )

    def clean_sms_code(self):
        sms_code = self.cleaned_data['sms_code']
        if sms_code != self.expected_sms_code:
            raise forms.ValidationError('Incorrect code.')
        return sms_code


def serialize_enrolment_forms(cleaned_data):
    """
    Return the shape directory-api-client expects for enrolment.

    @param {dict} cleaned_data - All the fields in `CompanyForm`, `UserForm`,
                                 `CorporateEmailAddressForm`,
                                 `CompanyNameForm`, and
                                 `CompanyExportStatusForm`
    @returns dict

    """

    return {
        'company_email': cleaned_data['company_email'],
        'company_name': cleaned_data['company_name'],
        'company_number': cleaned_data['company_number'],
        'mobile_number': cleaned_data['mobile_number'],
        'referrer': cleaned_data['referrer'],
        'export_status': cleaned_data['export_status'],
    }


def serialize_company_profile_forms(cleaned_data):
    """
    Return the shape directory-api-client expects for company profile edit.

    @param {dict} cleaned_data - All the fields in `CompanyBasicInfoForm`
                                 `CompanySizeForm`, `CompanyLogoForm`, and
                                 `CompanyClassificationForm`
    @returns dict

    """

    return {
        'name': cleaned_data['company_name'],
        'website': cleaned_data['website'],
        'keywords': cleaned_data['keywords'],
        'employees': cleaned_data['employees'],
        'sectors': json.dumps(cleaned_data['sectors']),
    }


def serialize_company_logo_forms(cleaned_data):
    """
    Return the shape directory-api-client expects for changing logo.

    @param {dict} cleaned_data - All the fields in `CompanyLogoForm`

    @returns dict

    """

    return {
        'logo': cleaned_data['logo'],
    }


def serialize_company_description_forms(cleaned_data):
    """
    Return the shape directory-api-client expects for changing description.

    @param {dict} cleaned_data - All the fields in `CompanyDescriptionForm`

    @returns dict

    """

    return {
        'description': cleaned_data['description'],
    }
