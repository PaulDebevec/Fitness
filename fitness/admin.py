from django.contrib import admin
from fitness.models import UserBMIProfile, UserProfile, MuscleGroup, WorkoutTracker, CardioWorkout


admin.site.register(UserBMIProfile)
admin.site.register(UserProfile)

admin.site.register(CardioWorkout)
admin.site.register(WorkoutTracker)
admin.site.register(MuscleGroup)

