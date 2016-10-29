from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm
from fitness.models import UserBMIProfile, UserProfile, WorkoutTracker


class BMIForm(forms.ModelForm):
    class Meta:
        model = UserBMIProfile
        fields = ('human_height_ft', 'human_height_in', 'weight')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_weight', 'user_height_ft', 'user_height_in')


class WorkoutTrackerForm(forms.ModelForm):
    class Meta:
        form = WorkoutTracker
        fields = '__all__'
