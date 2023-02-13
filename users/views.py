from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .forms import \
    UserRegistrationForm, \
    UserUpdateForm, \
    UserLoginForm, \
    ChangePasswordForm, \
    PasswordResetForm
from .decorators import user_not_authenticated
from .tokens import account_activation_token


def activate(request, uidb64, token):
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))  # docoding
        user = user.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('/')


def activate_email(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("users/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # primary key converter
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'  # for constructing a link
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please go to you email ({to_email}) inbox and click on \
                received activation link to confirm and complete the registration. Note: Check your spam folder.'
                         )
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, template_name='users/register.html', context=context)


@login_required
def my_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('/')


@user_not_authenticated
def my_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')

        for error in list(form.errors.values()):
            print(request, error)

    form = UserLoginForm()
    return render(
        request=request,
        template_name='users/login.html',
        context={'form': form}
    )


def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            print(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(
            request=request,
            template_name='users/profile.html',
            context={'form': form}
        )

    return redirect('/')


@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed.')
            return redirect('/login')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    form = ChangePasswordForm(user)
    return render(request, 'users/password_reset_confirm.html', context={'form': form})


@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("users/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                                     """
                                    Password reset sent \n
                                    We've emailed you instructions for setting your password, if an account exists with the email you entered.
                                    You should receive them shortly. \n If you don't receive an email, please make sure you've entered the address 
                                    you registered with, and check your spam folder.
                                    """
                                     )
                else:
                    messages.error(request, "Problem sending reset password email, SERVER PROBLEM")

            return redirect('/')

    form = PasswordResetForm()
    return render(
        request=request,
        template_name="users/password_reset.html",
        context={"form": form}
    )


def password_reset_confirm(request, uidb64, token):
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = ChangePasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and log in now.")
                return redirect('/')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = ChangePasswordForm(user)
        return render(request, 'users/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired.")

    messages.error(request, 'Something went wrong.')
    return redirect("/")
