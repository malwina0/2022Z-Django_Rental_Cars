from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django import forms
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Write your email here.", required=True)
    phone = forms.IntegerField(required=True)
    birth_date = forms.DateInput()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'birth_date', 'password1', 'password2']
        widgets = {
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
            })
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Write username or email'}
        ),
        label="Username or email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Write password'}
        ),
        label="Password"
    )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    birth_date = forms.DateInput()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'newpassword2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
