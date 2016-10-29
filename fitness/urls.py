from django.conf.urls import url
from django.views.generic import RedirectView
from fitness.views import *


urlpatterns = [
    url(r'^bmi/?$', bmi_view, name='bmi'),
    url(r'^profile/?$', user_profile_view, name='profile'),
    url(r'^login/?$', user_login, name='login'),
    url(r'^register/?$', register, name='register'),
    url(r'^dashboard/?$', index, name='dashboard'),
    url(r'^my_fitness/?$', my_fitness_view, name='my_fitness'),
    url(r'^trackworkout/?$', track_workout_view, name='trackwokout'),
    #url(r'^', my_fitness_view, name='dashboard')

    url(r'^$', RedirectView.as_view(pattern_name='dashboard', permanent=False))
]
