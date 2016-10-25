from django.conf.urls import url
from fitness.views import *

urlpatterns = [
    url(r'^bmi/$', bmi_view, name='bmi'),
    url(r'^profile/$', user_profile_view, name='profile'),
    url(r'^register/$', register, name='register'),
    #url(r'^login/$', user_login, name='login'),
    url(r'^dashboard/$', my_fitness_view, name='dashboard')
    #url(r'^$', name='home'),

]
