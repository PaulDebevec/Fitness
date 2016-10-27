from django.conf.urls import url
from fitness.views import *

urlpatterns = [
    url(r'^bmi/?$', bmi_view, name='bmi'),
    url(r'^profile/?$', user_profile_view, name='profile'),
    url(r'^register/?$', register, name='register'),
    url(r'^dashboard/?$', my_fitness_view, name='dashboard'),
    url(r'^my_fitness/?$', my_fitness_view, name='my_fitness'),
    url(r'^track_workout/?$', track_workout_view, name='track_wokout')
    #url(r'^', my_fitness_view, name='dashboard')
]
