from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class userregform(UserCreationForm):
    username=forms.CharField(max_length=50)
    password1=forms.CharField(max_length=15)
    password2=forms.CharField(max_length=15)
    phone_no=forms.CharField(max_length=20)
    First_Name=forms.CharField(max_length=20)
    Last_Name=forms.CharField(max_length=20)
    address=forms.CharField(max_length=10)
    state=forms.CharField(max_length=10)
    age=forms.IntegerField()

    class meta:
        model=User
        fields=['username','password 1','phone_no','email','password 2']

class bookform(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    company=forms.CharField(max_length=100)
    email=forms.EmailField
    menu=forms.CharField(max_length=50)
    bid=forms.IntegerField()
    start=forms.DateField()
    area_code=forms.IntegerField()
    phone=forms.IntegerField()
    subject=forms.Select()
    gender=forms.RadioSelect()
    card=forms.CharField(max_length=50)
    num=forms.CharField(max_length=16)
    cvv=forms.IntegerField(max_value=4)
    date=forms.DateField()
    price=forms.CharField(max_length=25)
   

class contactformemail(forms.Form):
    Email_address=forms.EmailField(required=True)
    Subject=forms.CharField(required=True)
    Message=forms.CharField(widget=forms.Textarea,required=True)
class hotelform(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    company=forms.CharField(max_length=100)
    email=forms.EmailField
    menu=forms.CharField(max_length=50)
    bid=forms.CharField(max_length=100)
    start=forms.DateField()
    area_code=forms.IntegerField()
    phone=forms.IntegerField()
    subject=forms.Select()
    Purpose=forms.CharField(max_length=100)
    Facility=forms.Select()
    gender=forms.RadioSelect()
   
   