from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário",)
    password = forms.CharField(label= "Senha", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    nome = forms.CharField(label = "Nome",)
    username = forms.CharField(label = "Usuário")
    email = forms.EmailField()
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Esse usuário já existe, escolha outro nome.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Esse email já existe, tente outro!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("As senhas informadas devem ser iguais!")
        return data