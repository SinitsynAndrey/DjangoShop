from django import forms

from mainapp.models import Products_categories, Products
from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm


class ShopUserAdminEditForm(ShopUserEditForm):

    class Meta:
        model = ShopUser
        fields = '__all__'


class CategoryAdminEditForm(forms.ModelForm):

    class Meta:
        model = Products_categories
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ProductAdminEditForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
