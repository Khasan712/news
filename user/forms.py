from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("first_name", 'email')

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password2 != password1:
            raise ValueError("Teng emas")
        user.set_password(password1)
        user.save()
        return user
