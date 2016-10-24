from django.conf.urls import url
from fitness.views import *

urlpatterns = [
    url(r'^bmi/$', bmi_view),
    url(r'^profile/$', user_profile_view),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^dashboard/$', dashboard, name='dashboard')
    #url(r'^$', dashboard, name='dashboard'),

]
