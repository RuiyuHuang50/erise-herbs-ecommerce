
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput


# Registration form

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # Mark email as required
        self.fields['email'].required = True
        
        # Add CSS classes to form fields
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'style': 'border-radius: 15px; padding: 1rem; border: 2px solid var(--border-light); font-size: 1.1rem;'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'style': 'border-radius: 15px; padding: 1rem; border: 2px solid var(--border-light); font-size: 1.1rem;'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'style': 'border-radius: 15px; padding: 1rem; border: 2px solid var(--border-light); font-size: 1.1rem;'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'style': 'border-radius: 15px; padding: 1rem; border: 2px solid var(--border-light); font-size: 1.1rem;'
        })


    # Email validation
    
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError('This email is invalid')

        # len function updated ###

        if len(email) >= 350:

            raise forms.ValidationError("Your email is too long")


        return email



# Login form

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'style': 'border-radius: 15px; padding: 1rem; border: 2px solid var(--border-light); font-size: 1.1rem;'
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'style': 'border-radius: 15px; padding: 1rem; border: 2px solid var(--border-light); font-size: 1.1rem;'
    }))



# Update form

class UpdateUserForm(forms.ModelForm):

    password = None


    class Meta:

        model = User

        fields = ['username', 'email']
        exclude = ['password1', 'password1']
    

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        # Mark email as required

        self.fields['email'].required = True

        
    # Email validation
    
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():

            raise forms.ValidationError('This email is invalid')

        # len function updated ###

        if len(email) >= 350:

            raise forms.ValidationError("Your email is too long")


        return email
        
        
 
 

    