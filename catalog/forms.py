from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        if cleaned_name in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']:
            raise forms.ValidationError("Вы не можете добавить продукт c таким именем")
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        if cleaned_description in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']:
            raise forms.ValidationError("Вы не можете добавить продукт c таким описанием")
        return cleaned_description
