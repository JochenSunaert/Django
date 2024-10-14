# myapp/forms.py
from django import forms
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']  # Fields that will be displayed in the form


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser  # Ensure this is referencing the CustomUser model
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already taken.")
        return email