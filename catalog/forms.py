from django import forms
from catalog.models import Product, Version
from django.forms import BooleanField


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.fields.items():

            if isinstance(v, BooleanField):
                v.widget.attrs['class'] = 'form-check-input'
            else:
                v.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner',]

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        if cleaned_name in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']:
            raise forms.ValidationError("Вы не можете добавить продукт c таким именем")
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        if cleaned_description in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                   'полиция',
                                   'радар']:
            raise forms.ValidationError("Вы не можете добавить продукт c таким описанием")
        return cleaned_description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
