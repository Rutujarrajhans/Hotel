from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=20,blank=False)
    password=models.CharField(max_length=8,blank=False)
    

    def __str__(self):
        return self.username

class register(models.Model):
    username=models.CharField(max_length=50)
    password1=models.CharField(max_length=15)
    password2=models.CharField(max_length=15)
    phone_no=models.CharField(max_length=50)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    
    address=models.CharField(max_length=5)
    age=models.CharField(max_length=5)
    state=models.CharField(max_length=5)
    
    email=models.EmailField(max_length=10)
    def __str__(self):
        return self.username


class Menu(models.Model):
    m_name=models.CharField(max_length=7,primary_key=True)
    menu_type=models.CharField(max_length=9,blank=True)
    def __str__(self):
        return self.m_name

class Boopay(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    company=models.CharField(max_length=100)
    email=models.EmailField(max_length=25)
    menu=models.CharField(max_length=25)
    bid=models.IntegerField(blank=False)
    start=models.DateField()
    area_code=models.IntegerField()
    phone=models.IntegerField()
    subject=models.CharField(max_length=25)
    gender=models.CharField(max_length=2)
    card=models.CharField(primary_key=True,max_length=50)
    num=models.CharField(max_length=16)
    cvv=models.IntegerField(max_length=4)
    date=models.DateField()
    price=models.CharField(max_length=25)
   
    def __str__(self):
        return self.price
class Hotel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    company=models.CharField(max_length=100)
    email=models.EmailField(max_length=25)
    menu=models.CharField(max_length=25)
    bid=models.CharField(max_length=50)
    start=models.CharField(max_length=25)
    area_code=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    subject=models.CharField(max_length=25)
    Facility=models.CharField(max_length=25)
    gender=models.CharField(max_length=2)
   
    Purpose=models.CharField(max_length=100)
   
   
    def __str__(self):
        return self.first_name
class Living(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
   
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.CharField(max_length=50,default=12)
    def __str__(self):
        return self.room_type

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
   
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.booking_id