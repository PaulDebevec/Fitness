from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models




class UserBMIProfile(models.Model):
    human_height_ft = models.IntegerField(help_text='Enter height in feet')
    human_height_in = models.IntegerField(help_text='Enter height in inches')
    human_weight = models.FloatField(help_text='Enter weight in pounds')


    def __unicode__(self):
        return 'User BMI - %s' % self.body_mass_calc()

    #function to calculate body mass
    def body_mass_calc(self):
        weight = self.human_weight        #human weight in pounds
        weight_in_kg = float(weight / 2.2)      #converts human weight from pounds to kilograms
        height_ft = self.human_height_ft        #human height in feet
        height_in = self.human_height_in        #human height in inches
        height_total_in = float((height_ft * 12) + height_in) #converts feet to inches and produces total hight in inches
        height_in_m = float(height_total_in * .0254)         #converts human height from inches to meters
        body_mass = float(weight_in_kg / (height_in_m * 2))    #calculates BMI
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


class UserWeight(models.Model):
    user = models.ForeignKey(User)
    user_weight = models.FloatField(help_text='Enter weight in pounds')
    weight_date = models.DateField(auto_now=False, auto_now_add=False)

