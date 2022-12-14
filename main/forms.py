from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    user_email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "user_email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        # call email attribute of user object as user.email
        # anything else would result in the email not being saved
        user.email = self.cleaned_data["user_email"]
        if commit:
            user.save()
        return user


class ListCreationForm(forms.Form):
    list_name = forms.CharField(label=False, max_length=100,
                                widget=forms.TextInput(attrs={"placeholder": "Enter your list name"}))


class TaskCreationForm(forms.Form):
    task_name = forms.CharField(label=False, max_length=100,
                                widget=forms.TextInput(attrs={"placeholder": "Enter your task name"}))
    task_checkbox = forms.CheckboxInput(check_test=None)
