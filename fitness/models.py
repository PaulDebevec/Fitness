from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

LIFTING_CARDIO = (('Lifting', 'Lifting'),
                  ('Cardio', 'Cardio'))

MUSCLE_GROUP = (('Chest', 'Chest'),
                ('Back', 'Back'),
                ('Shoulders', 'Shoulders'),
                ('Abs', 'Abs'),
                ('Legs', 'Legs'),
                ('Arms', 'Arms'))

CARDIO_TYPE_WORKOUT = (('Running', 'Running'),
                       ('Biking', 'Biking'))

LIFTING_TYPE = (('Bench press', 'Bench Press'),
                ('Chest fly', 'Chest fly'),
                ('Dips Machine fly', 'Dips Machine fly'),
                ('Push-up', 'Push-up'),
                ('Chin-up', 'Chin-up'),
                ('Pulldown', 'Pulldown'),
                ('Pull-up', 'Pull-up'),
                ('Shoulder shrug', 'Shoulder shrug'),
                ('Shoulder press', 'Shoulder press'),
                ('Biceps Curl', 'Biceps Curl'),
                ('Chin-up', 'Chin-up'),
                ('Close-grip bench press', 'Close-grip bench press'),
                ('Dips', 'Dips'),
                ('Triceps extension', 'Triceps extension'),
                ('Forearms', 'Forearms'),
                ('Crunch', 'Crunch'),
                ('Leg raise', 'Leg raise'),
                ('Russian twist', 'Russian twist'),
                ('Sit-up', 'Sit-up'),
                ('Deadlift', 'Deadlift'))


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_weight = models.IntegerField(verbose_name='Your weight:', help_text='Enter weight in pounds', default=150)
    user_height_ft = models.IntegerField(verbose_name='Your height in feet:', default=5)
    user_height_in = models.IntegerField(verbose_name='Your height in inches:', default=10)
    date = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.user.username


class UserBMIProfile(models.Model):
    human_height_ft = models.IntegerField(verbose_name='Height', help_text='Enter height in feet')
    human_height_in = models.IntegerField(verbose_name='Inches', help_text='Enter height in inches')
    weight = models.IntegerField(verbose_name='Weight', default=150, help_text='Enter weight in pounds')
    profile = models.ForeignKey(UserProfile)
    def __unicode__(self):
        return 'User BMI - {}'.format(self.body_mass_calc())

    #function to calculate body mass
    def body_mass_calc(self):
        weight_in_kg = self.weight / 2.2  #converts human weight from pounds to kilograms
        height_total_in = self.human_height_ft * 12 + self.human_height_in #converts feet to inches and produces total hight in inches
        height_in_m = height_total_in * .0254       #converts human height from inches to meters
        body_mass = weight_in_kg / (height_in_m * 2)  #calculates BMI
        return round(body_mass, 1)

    @property
    def bmi_feedback(self): #Returns/displays BMI results
        bmi_string = "Your BMI is %s. A healthy average is between 18.5 and 25." % self.body_mass_calc()
        if self.body_mass_calc() < 18.5:
            return bmi_string
        elif self.body_mass_calc() >= 18.5 and self.body_mass_calc() < 25:
            return "Your BMI is %s, you are average." % self.body_mass_calc()
        elif self.body_mass_calc() >= 25 and self.body_mass_calc() < 30:
            return bmi_string
        elif self.body_mass_calc() >= 30:
            return bmi_string


class CardioWorkout(models.Model):
    exercise_type = models.CharField(max_length=5, choices=CARDIO_TYPE_WORKOUT)
    distance = models.FloatField(default=1)
    date = models.DateField(auto_now_add=True)


class MuscleGroup(models.Model):
    muscle_group = models.CharField(max_length=5, choices=MUSCLE_GROUP)


class WorkoutTracker(models.Model):
    muscle_group = models.CharField(max_length=5, choices=MUSCLE_GROUP)
    lift_type = models.CharField(max_length=25, choices=LIFTING_TYPE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    assisted = models.BooleanField(default=False)
    raw_weight = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return '{} sets, {} reps, with {} weight.'.format(self.sets, self.reps, self.raw_weight)




"""
class WorkoutType(models.Model):
    exercise_type = models.CharField(max_length=5, choices=LIFTING_CARDIO)
    cardio_type = models.CharField(max_length=5, choices=CARDIO_TYPE_WORKOUT)
    muslce_group = models.CharField(max_length=5, choices=MUSCLE_GROUP)


class WorkoutTracker(models.Model):
    reps = models.IntegerField(default=5)
    distance = models.FloatField(default=1)
    weight = models.IntegerField()

"""
