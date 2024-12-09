from django import forms
from .models import studentModel

class studentForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = '__all__'

        # labels = {
        #     'name' : 'Student name',
        #     'roll' : 'Student roll'
        # }

        # widgets = {
        #     'name' : forms.TextInput(attrs={'class':'btn-primary'}),
        #     'roll' : forms.PasswordInput()
        # }

        # help_texts = {
        #     'name' : 'Write your full name'
        # }

        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }

