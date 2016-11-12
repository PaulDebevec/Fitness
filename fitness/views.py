from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from fitness.forms import BMIForm, UserProfileForm, UserForm, AddWorkoutForm
from fitness.models import UserBMIProfile, UserProfile, AddWorkout


def index(request):
    display = 'Test'
    context = {
        'display': display
    }
    return render(request, 'base.html', context)


@login_required(login_url='/login/')
def my_fitness_view(request):
    form = AddWorkoutForm(request.POST)
    profile = UserProfile.objects.get(user=request.user)
    f_obj = AddWorkout.objects.filter(user=profile)
    contains = {
            'profile': profile,
            'f_obj': f_obj,
            'form': form,
            }
    return render(request, 'my_fitness.html', contains)


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
            bmi_profile = UserBMIProfile(profile=profile,
                                         human_height_ft=profile.user_height_ft,
                                         human_height_in=profile.user_height_in,
                                         weight=profile.user_weight)
            bmi_profile.save()
            return HttpResponseRedirect('/fitness/login/')
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
        return render(request, 'login.html', )


@login_required(login_url='/login/')
def bmi_view(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BMIForm()
    bmi_get = UserBMIProfile.objects.get(profile__user=request.user)
    context = {
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
    user_get = UserProfile.objects.filter(user__user=request.user)
    contains = {
        'user_get': user_get,
        'form': form,
        }
    return render(request, 'profile.html', contains)


@login_required(login_url='/login/')
def add_workout_view(request):
    if request.method == 'POST':
        workout_form = AddWorkoutForm(request.POST)
        if workout_form.is_valid():
            save_workout = workout_form.save(commit=False)
            profile = UserProfile.objects.get(user=request.user)
            save_workout.user = profile
            save_workout.save()
        return render(request, 'track_workout.html')
    else:
        workout_form = AddWorkoutForm()
    user = request.user
    context = {
        'form': workout_form,
        'user': user,
    }
    return render(request, 'track_workout.html', context)



"""
if request.method == 'POST':
        workout = WorkoutTrackerForm(data=request.POST)
        form = WorkoutTracker()
        contains = {
            'workout': workout,
            'form': form,
            }
        return render(request, 'track_workout.html', contains)

# user = 'user__user=request.user'
            # if workout_form.is_valid():
            #     date_workout.save()
            #     workout_form.save()


"""
