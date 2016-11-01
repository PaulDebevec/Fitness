from django.contrib import admin

from fitness.models import UserBMIProfile, UserProfile, AddWorkout, CardioWorkout

#BMI/User Profile registries
admin.site.register(UserBMIProfile)
admin.site.register(UserProfile)

#Workout registries
admin.site.register(CardioWorkout)
admin.site.register(AddWorkout)

