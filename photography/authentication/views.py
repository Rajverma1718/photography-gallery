from django.shortcuts import render, HttpResponseRedirect # type: ignore
from .forms import SignUpForm, LoginForm # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm # type: ignore
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash # type: ignore

#ADMIN PANEL USERNAME:admin, PASSWOARD: admin
# Create your views here.


#SIGNUP VIEW FUNCTION
def sign_up(request, context=None):
    if not request.user.is_authenticated:
        context = context or {}
        context['signup'] = 'active'

        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                messages.success(request, 'Your account was created Successfully. Please Login to continue!!')
                fm.save()
                return HttpResponseRedirect('/login/')
        else:
            fm = SignUpForm()

        context['form'] = fm
        # return render(request, 'auth/signup.html',  {'form': fm})  
        return render(request, 'signup.html', context)  
    else:
        return HttpResponseRedirect('/dashboard/')


#LOGIN VIEW FUNCTION
def user_login(request, context=None):
    if not request.user.is_authenticated:
        context = context or {}
        context['login'] = 'active'

        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/dashboard/')
                # else:
                #     messages.error(request, 'Invalid username or password.')
        else:
            fm = LoginForm()

        context['form'] = fm
        # return render(request, 'auth/user_login.html',  {'form': fm})
        return render(request, 'user_login.html', context)
    else:
        return HttpResponseRedirect('/dashboard/')


#LOGOUT VIEW FUNCTION
def user_logout(request):
    logout(request)
    messages.success(request, 'Log-out successfully !!')
    return HttpResponseRedirect('/login/')

#CHANGE PASSWORD WITH OLD PASSWORD
def user_change_pass(request, context=None):
    if request.user.is_authenticated:
        context = context or {}
        context['changepass'] = 'active'
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Passwoard Change Successfully !!')
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/changepass/')
        else:
            fm = PasswordChangeForm(user=request.user)

        context['form'] = fm
        # return render(request, 'auth/changepass.html',  {'form': fm})
        return render(request, 'changepass.html', context)
    else:
        return HttpResponseRedirect('/login/')

#FORGATE PASSWORD WITH OLD PASSWORD
def user_new_pass(request, context=None):
    if request.user.is_authenticated:
        context = context or {}
        context['newpass'] = 'active'
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'New Passwoard Set Successfully !!')
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/newpass/')
        else:
            fm = SetPasswordForm(user=request.user)

        context['form'] = fm
        # return render(request, 'auth/forgot.html', {'form': fm})
        return render(request, 'forgot.html', context)
    else:
        return HttpResponseRedirect('/login/')