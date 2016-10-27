from django.contrib import admin

from fitness.models import UserBMIProfile, UserProfile, MuscleGroup, \
    WorkoutTracker, CardioWorkout

#BMI/User Profile registries
admin.site.register(UserBMIProfile)
admin.site.register(UserProfile)

#Workout registries
admin.site.register(CardioWorkout)
admin.site.register(WorkoutTracker)
admin.site.register(MuscleGroup)

