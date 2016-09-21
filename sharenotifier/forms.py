from django import forms


class LoginForm(forms.Form):
    user_name = forms.EmailField(label='User Name', max_length=50)
    pass_word = forms.CharField(label='Password', widget=forms.PasswordInput())