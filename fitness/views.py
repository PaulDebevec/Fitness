from django.shortcuts import render
from fitness.forms import BMIForm
from fitness.models import UserBMIProfile, UserWeight



def bmi_view(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BMIForm()
        bmi_all = UserBMIProfile.objects.all()
        bmi_get = UserBMIProfile.objects.get(id=1) #request.user.id - connect user model to profile model
        context = {
        'bmi_all': bmi_all,
        'bmi_get': bmi_get,
        'form': form,
        }
    return render(request, 'base.html', context)


def user_weight_view(request):
    if request.method == 'POST':
        form = UserWeight(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserWeight()
        weight_all = UserWeight.objects.all()
        weight_get = UserWeight.objects.get(id=1)
        context = {
            'weight_all': weight_all,
            'weight_get': weight_get,
            'form': form,
        }
    return render(request, 'weight.html', context)