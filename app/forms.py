from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import request

from app.models import Profile, Question


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again")
        return self.cleaned_data
        # if self.cleaned_data['username'] != self.cleaned_data['password']:
        #     raise ValidationError('Username and password do not match')

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    #image = forms.ImageField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password']

    def clean(self):
        super().clean()
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('Username and password do not match')

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        profile = Profile(
            nick_name= user,
            name=user.username,
            rate=0
        )
        profile.save()
        return user

class AskForm(forms.Form):
    header = forms.CharField()
    content = forms.CharField(widget=forms.Textarea())
    tag = forms.CharField()
    def clean(self):
        super().clean()
        if self.cleaned_data['header'] == "":
            raise ValidationError('header is empty!')
        if self.cleaned_data['content'] == "":
            raise ValidationError('content is empty!')

class AnswerForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())

    def clean(self):
        super().clean()
        if self.cleaned_data['content'] == "":
            raise ValidationError('content is empty!')

class EditProfile(forms.Form):
    nickname = forms.CharField()
    image = forms.ImageField()

    def clean(self):
        if self.cleaned_data['nickname'] == "":
            raise ValidationError('content is empty!')
