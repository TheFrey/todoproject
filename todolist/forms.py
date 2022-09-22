from django import forms
from django.contrib.auth.models import User
from .models import ToDoItem, SubItem


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):
        cd = self.cleaned_data
        a = cd['password']
        if len(a) >=8 and any(map(str.isupper, a)) and any(map(str.islower, a)) and any(map(str.isdigit, a)):
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            else:
                return cd['password2']
        else:
            raise forms.ValidationError('Need upper, lower and digit symbol')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TodoItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('text', 'urgency')


class SubItemForm(forms.ModelForm):
    class Meta:
        model = SubItem
        fields = ('text', )


