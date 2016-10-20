from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from fitness.forms import BMIForm, UserProfileForm, UserForm
from fitness.models import UserBMIProfile, UserProfile



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
        #     if 'picture' in request.FILES:
        #         profile.picture = request.FILES['picture']
        #     profile.save()
        #     registered = True
        # else:
        #     print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form,
             'registered': registered} )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/fitness/')
            else:
                return HttpResponse("Your fitness account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})


@login_required(login_url='/login/')
def bmi_view(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BMIForm()
        bmi_all = UserBMIProfile.objects.all()
        bmi_get = UserBMIProfile.objects.get(user=request.user)
        context = {
        'bmi_all': bmi_all,
        'bmi_get': bmi_get,
        'form': form,
        }
    return render(request, 'base.html', context)


def user_weight_view(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserProfile()
        weight_all = UserProfile.objects.all()
        weight_get = UserProfile.objects.get(id=1)
        context = {
            'weight_all': weight_all,
            'weight_get': weight_get,
            'form': form,
        }
    return render(request, 'weight.html', context)



