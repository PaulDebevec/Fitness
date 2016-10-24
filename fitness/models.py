from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


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



