from django.shortcuts import render
from temp_url.forms import UserForm, UserProfileInfoForm
#for login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def index2(request):
    return render(request, 'temp_url/index2.html')

def base(request):
    return render(request, 'temp_url/base.html')

def other(request):
    context_dict={'text':'Hello world', 'number':100}
    return render(request, 'temp_url/other.html', context_dict)

def relative(request):
    return render(request, 'temp_url/relative_url_templates.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'temp_url/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('temp_url:index2'))
            else:
                return HttpResponse('Account is not active')
        else:
            print('Failed')
            print('Username: {} and password: {}'.format(username, password))
            return HttpResponse('Invalid login or password')
    else:
        return render(request, 'temp_url/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('temp_url:index2'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")
