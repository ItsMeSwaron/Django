from django import forms
from .models import Brands

class brandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = '__all__'