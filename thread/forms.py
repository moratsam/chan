from django import forms
from django.contrib.auth import authenticate, get_user_model, login

from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model=Thread
        fields=[
            "title",
            "image",
            "content",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=[
            "image",
            "content",
        ]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user=authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("user does not exist")
        if not user.check_password(password):
            raise forms.ValidationError("incorrect password")
        if not user.is_active:
            raise forms.ValidationError("user no longer active")
        return super(LoginForm, self).clean()

