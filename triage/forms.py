from collections import namedtuple

from directory_constants.constants import exred_sector_names

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH

from core.widgets import RadioSelect
from triage import fields


Persona = namedtuple('Persona', ['name', 'label'])
REGULAR_EXPORTER = Persona(name='REGULAR_EXPORTER', label='Regular exporter')
OCCASIONAL_EXPORTER = Persona(
    name='OCCASIONAL_EXPORTER', label='Occasional exporter'
)
NEW_EXPORTER = Persona(name='NEW_EXPORTER', label='New exporter')
SECTORS_CHOICES = [
    (value, value + ' ' + label)
    for value, label in exred_sector_names.SECTORS_CHOICES
]


class BaseTriageForm(forms.Form):
    use_required_attribute = False
    error_css_class = 'input-field-container has-error'


class SectorForm(BaseTriageForm):
    sector = forms.ChoiceField(
        choices=BLANK_CHOICE_DASH + SECTORS_CHOICES,
        label='What do you want to export?',
        label_suffix='',
        widget=forms.Select(attrs={'id': 'js-sector-select'}),
    )


class ExportExperienceForm(BaseTriageForm):
    exported_before = forms.TypedChoiceField(
        label='Have you exported before?',
        label_suffix='',
        coerce=lambda x: x == 'True',
        choices=[(True, 'Yes'), (False, 'No')],
        widget=RadioSelect(),
    )


class RegularExporterForm(BaseTriageForm):
    regular_exporter = forms.TypedChoiceField(
        label='Is exporting a regular part of your business activities?',
        label_suffix='',
        coerce=lambda x: x == 'True',
        choices=[(True, 'Yes'), (False, 'No')],
        widget=RadioSelect(),
        required=False,
        empty_value=None,
    )


class OnlineMarketplaceForm(BaseTriageForm):
    used_online_marketplace = forms.TypedChoiceField(
        label='Do you use online marketplaces to sell your products?',
        label_suffix='',
        coerce=lambda x: x == 'True',
        choices=[(True, 'Yes'), (False, 'No')],
        widget=RadioSelect(),
        required=False,
        empty_value=None,
    )


class CompanyForm(BaseTriageForm):
    company_name = forms.CharField(
        label='What is your company name? (optional)',
        help_text="We'll use this information to personalise your experience",
        label_suffix='',
        max_length=1000,
        widget=forms.TextInput(
            attrs={'id': 'js-typeahead-company-name'}
        ),
        required=False,
    )
    company_number = fields.PaddedCharField(
        label='Company number:',
        max_length=8,
        fillchar='0',
        widget=forms.HiddenInput(attrs={'id': 'js-typeahead-company-number'}),
        required=False,
    )

    def clean_company_number(self):
        number = self.cleaned_data['company_number']
        if number == '':
            return None
        return number


class CompaniesHouseForm(BaseTriageForm):
    is_in_companies_house = forms.TypedChoiceField(
        label='Is your company incorporated in the UK?',
        label_suffix='',
        coerce=lambda x: x == 'True',
        choices=[(True, 'Yes'), (False, 'No')],
        widget=RadioSelect(),
        required=False,
        empty_value=None,
    )


class SummaryForm(forms.Form):
    pass


class CompaniesHouseSearchForm(forms.Form):
    term = forms.CharField()


def get_persona(cleaned_data):
    is_regular_exporter = cleaned_data.get('regular_exporter') is True
    has_exported_before = cleaned_data.get('exported_before') is True

    if is_regular_exporter:
        return REGULAR_EXPORTER
    elif not is_regular_exporter and has_exported_before:
        return OCCASIONAL_EXPORTER
    return NEW_EXPORTER


def get_has_exported_before(answers):
    return answers.get('exported_before') is True


def get_is_regular_exporter(answers):
    return answers.get('regular_exporter') is True


def get_is_in_companies_house(answers):
    return answers.get('is_in_companies_house') is True


def get_used_marketplace(answers):
    return answers.get('used_online_marketplace') is True


def get_sector_label(cleaned_data):
    for key, label in exred_sector_names.SECTORS_CHOICES:
        if key == cleaned_data['sector']:
            return label


def serialize_triage_form(data):
    return {
        'sector': data['sector'],
        'exported_before': data['exported_before'],
        'regular_exporter': data.get('regular_exporter'),
        'used_online_marketplace': data.get('used_online_marketplace'),
        'company_name': data.get('company_name', ''),
        'company_number': data.get('company_number'),
        'is_in_companies_house': data['is_in_companies_house'],
    }
