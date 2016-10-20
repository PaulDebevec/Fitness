from django.forms import ModelForm
from fitness.models import UserBMIProfile, UserWeight


class BMIForm(ModelForm):
    class Meta:
        model = UserBMIProfile
        fields = ('human_weight', 'human_height_ft', 'human_height_in', )


class UserWeightForm(ModelForm):
    class Meta:
        model = UserWeight
        fields = ('user_weight', 'weight_date', 'user', )

