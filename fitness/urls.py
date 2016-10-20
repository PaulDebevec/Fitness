from django.conf.urls import url
from fitness.views import *

urlpatterns = [
    url(r'^bmi/$', bmi_view),

]
