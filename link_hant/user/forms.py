from django import forms
from user.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields = ("username", "password")
        widgets = {
            "password": forms.PasswordInput()
        }

    def clean(self):
        return self.cleaned_data