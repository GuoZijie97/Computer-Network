from django import forms
from django.contrib.auth.models import User
import re


def email_check(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0

    # pattern = re.compile("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$")
    # return re.match(pattern, email)


class RegistrationForm(forms.Form):

    username = forms.CharField(label='用户名', max_length=50)
    email = forms.EmailField(label='邮箱',)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    # Use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("Your username must be at least 6 characters long.")
        elif len(username) > 50:
            raise forms.ValidationError("Your username is too long.")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your username already exists.")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your email already exists.")
        else:
            raise forms.ValidationError("Please enter a valid email.")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("Your password is too short.")
        elif len(password1) > 20:
            raise forms.ValidationError("Your password is too long.")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch. Please enter again.")

        return password2


class LoginForm(forms.Form):

    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)

    # Use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if email_check(username):
            filter_result = User.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError("This email does not exist.")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError("This username does not exist. Please register first.")

        return username


class ProfileForm(forms.Form):

    first_name = forms.CharField(label='名字', max_length=50, required=False)
    last_name = forms.CharField(label='姓氏', max_length=50, required=False)
    studentno = forms.CharField(label= '学号', max_length=50,  required=True)
    org = forms.CharField(label='院系', max_length=50, required=False)
    telephone = forms.CharField(label='电话', max_length=50, required=False)
    wechat = forms.CharField(label='微信号', max_length=50, required=False)


class PwdChangeForm(forms.Form):
    old_password = forms.CharField(label='旧密码', widget=forms.PasswordInput)

    password1 = forms.CharField(label='新密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认新密码', widget=forms.PasswordInput)

    # Use clean methods to define custom validation rules

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("Your password is too short.")
        elif len(password1) > 20:
            raise forms.ValidationError("Your password is too long.")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch. Please enter again.")

        return password2
