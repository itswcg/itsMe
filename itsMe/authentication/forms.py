from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               max_length=30,
                               required=True,
                               label='用户名')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                            max_length=50,
                            required=True,
                            label='邮箱')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='密码',
                               required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='确认密码',
                               required=True)
    captcha = CaptchaField(label='验证码')

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(['密码不匹配'])
        return self.cleaned_data