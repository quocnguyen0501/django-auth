from django import forms
from authentication.entities.User import User


class RegistrationForm(forms.Form):
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  phone = forms.CharField(max_length=30)
  name = forms.CharField(max_length=255)

  def check_email(self):
    email = self.cleaned_data['email']

    if User.objects.filter(email=email).exists():
      raise forms.ValidationError("User existed.")

    return email
