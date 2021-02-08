from django import forms
from home.models import QuickContact


class QuickContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="User name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name *",
            }
        ),
    )
    email = forms.EmailField(
        label="User email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Email *"},
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Message *",
                "rows": 3,
            }
        )
    )

    def save(self):
        QuickContact.objects.create(**self.cleaned_data)

    def clean(self):
        print("VALIDACIYA!!!")
        return self.cleaned_data


class QuickForm(forms.ModelForm):
    
    class Meta:
        model=QuickContact
        fields = "__all__"