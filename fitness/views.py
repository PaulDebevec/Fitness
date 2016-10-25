from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from fitness.forms import BMIForm, UserProfileForm, UserForm
from fitness.models import UserBMIProfile, UserProfile

#request.user


def my_fitness_view(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        contains = {
            'user_all': UserProfile.objects.all(),
            #'user_get': UserProfile.objects.get(user=request.user),
            'form': form,
        }
    if request.method == 'GET':
        contains = {
            'user_all': UserProfile.objects.all(),
            #'user_get': UserProfile.objects.get(user=request.user),
        }
    return render(request, 'dashboard.html', contains)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/fitness/dashboard')
            else:
                return HttpResponse("Your fitness account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html',)


@login_required(login_url='/login/')
def bmi_view(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BMIForm()
        bmi_all = UserBMIProfile.objects.all()
        bmi_get = UserBMIProfile.objects.get(profile__user=request.user)
        context = {
            'bmi_all': bmi_all,
            'bmi_get': bmi_get,
            'form': form,
        }
    return render(request, 'bmi.html', context)


@login_required(login_url='/login/')
def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserProfile()
        user_all = UserProfile.objects.all()
        user_get = UserProfile.objects.get(user=request.user)
        contains = {
            'user_all': user_all,
            'user_get': user_get,
            'form': form,
        }
    return render(request, 'profile.html', contains)


# def dashboard(request):
#     user_name = user.
#     user_height
#     user_weight
#     user_bmi
#
#     return render(request, 'dashboard.html', display)
#
#
