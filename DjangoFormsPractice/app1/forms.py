from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label='Username', initial='Hello', help_text='Enter your name', required=False, disabled=True, widget=forms.Textarea) 
    # file = forms.FileField()
    email = forms.EmailField(label='User email') 
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    # dateOfBirth = forms.DateField(label='Date of birth')
    dateOfBirth = forms.DateField(label='Date of birth', widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL = [('P','Pepperoni'),('M','Mushroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']

    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name should be at least 10 characters')
        
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']

    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Your email must have .com')
        
    #     return valemail
    
    # def clean(self):
        
    #     cleaned_data = super().clean()

    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']

    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name should be at least 10 characters')
        
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Your email must have .com')
        

def errorChecker(val):
    
    if len(val) < 10:
        raise forms.ValidationError('Enter a value with 10 chars')

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(validators=[validators.MinValueValidator(20,message='Age must be greater than 19'), validators.MaxValueValidator(30,message='Age must be less than 31')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='allowed extension is .pdf')])
    text = forms.CharField(widget=forms.TextInput, validators=[errorChecker])

class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)

    def clean(self):

        cleaned_data = super().clean()

        valPassword = cleaned_data['password']
        valConfirmPassword = cleaned_data['confirmPassword']

        if valPassword != valConfirmPassword:
            raise forms.ValidationError('Password did not match')
    