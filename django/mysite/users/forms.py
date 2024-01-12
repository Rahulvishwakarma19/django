from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CusOrders, CusRatingFeedback

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CusOrdersUpd(forms.ModelForm):
    class Meta:
        model = CusOrders
        fields = ['order_id', 'prod_code', 'quantity', 'user']

class CusRatFeedForm(forms.ModelForm):
    class Meta:
        model = CusRatingFeedback
        fields = ['ratings', 'feedback']