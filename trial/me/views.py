from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import userregform
from .forms import bookform
from .forms import contactformemail
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import generic
from django.views.generic import TemplateView,ListView
from.serializers import MenuSerializer
from.models import Login,register,Menu,Boopay,Hotel,Living,Reservation
from operator import itemgetter
import sqlite3
from django.contrib.auth.decorators import login_required
import datetime
import json


def index(request):
    return render(request,'me/index.html')
def well(request):
    

    
    
    if request.method =="POST":

        form=userregform(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            h=get_template('me/Email.html')
            d={'name':name}
            subject,from_email,to='welc',"2018.rutuja.rajhas@gmail.com",email
            cont=h.render(d)
            msg=EmailMultiAlternatives(subject,from_email,cont,[to])
            msg.attach_alternative(cont,"text/html")
            msg.send()
            messages.success(request,f"congrats")
            
            return redirect('login')
    else:
        form=userregform()
    return render(request,'me/repeater.html',{'form':form})

    


    
def acess(request):
    if request.method=="POST":
        
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        username=request.POST.get('username','')
        password1=request.POST.get('password','')
        lo_obj=Login(username=username,password=password)
        lo_obj.save()
        if user is not None:
            form=login(request,user)
            messages.success(request,f'hey {username}')
            return redirect('index')
        else:
           
            messages.info(request,f'account not exists,sign in')
            
    form=AuthenticationForm()
    return render(request,'me/login.html',{'form':form,'title':'log in'})
def menu(request):


    return render(request,'me/menu.html')

class Menulist(APIView):
    
    def get(self,request):
        Menu1=Menu.objects.all()
        serializer=MenuSerializer(Menu1,many=True)
        return Response(serializer.data)
       
    def post(self,request):
        
        pass
def bookView(request):
    return render(request,'me/book.html')
def booksub(request):

    first_name=request.POST.get('first_name','')
    last_name=request.POST.get('last_name','')
    company=request.POST.get('company','')
    email=request.POST.get('email','')
    menu=request.POST.get('menu','')
    bid=request.POST.get('bid','')

    start=request.POST.get('start','')

    area_code=request.POST.get('area_code','')

    phone=request.POST.get('phone','')

    subject=request.POST.get('subject','')

    gender=request.POST.get('gender','')

    card=request.POST.get('card','')

    num=request.POST.get('num','')
    cvv=request.POST.get('cvv','')
    date=request.POST.get('date','')
    price=request.POST.get('price','')

    book_oj=Boopay(first_name=first_name,last_name=last_name,company=company,email=email,menu=menu,bid=bid,start=start,area_code=area_code,phone=phone,subject=subject,gender=gender,card=card,num=num,cvv=cvv,date=date,price=price)
    book_oj.save()
    print("successful")
    return render(request,'me/index.html')


def emailsending(request):
    if request.method=="GET":
        form=contactformemail()
    else:
        form=contactformemail(request.POST)
        if form.is_valid():
            fromemail=form.cleaned_data['fromemail']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail(subject,message,fromemail,['2018.rutuja.rajhans@ves.ac.in',fromemail])
            return redirect('index')
        else:
            pass
    return render(request,'me/msg.html',{'form':form})       

    
def about(request):
    return render(request,'me/about.html')

def hotel(request):
    first_name=request.POST.get('first_name','')
    last_name=request.POST.get('last_name','')
    company=request.POST.get('company','')
    email=request.POST.get('email','')
    menu=request.POST.get('menu','')
    bid=request.POST.get('bid','')

    

    area_code=request.POST.get('area_code','')

    phone=request.POST.get('phone','')

    subject=request.POST.get('subject','')

    gender=request.POST.get('gender','')

    Purpose=request.POST.get('Purpose','')

    Facility=request.POST.get('Facility','')
    

    hotel_oj=Hotel(first_name=first_name,last_name=last_name,company=company,email=email,menu=menu,bid=bid,area_code=area_code,phone=phone,subject=subject,gender=gender,Purpose=Purpose,Facility=Facility)
    hotel_oj.save()
    print("successful")
    return render(request,'me/room.html')


class Liviing(generic.ListView):
    template_name='me/panel.html'
    total_rooms = Living.objects.all()
    
    
    available=total_rooms.filter(status="1").count()
    unavailable=total_rooms.filter(status="2").count()

    context={}
    context={'total_rooms':total_rooms,'available':available,'unavailable':unavailable}
    def get_queryset(request):

        

       
        return Living.objects.all()
    def go(request):
        return render(request,"me/delete.html")

   
    
def getu(request):
   
    total_rooms = Living.objects.all()
    
    
    available=total_rooms.filter(status="1").count()
    unavailable=total_rooms.filter(status="2").count()
    context={'total_rooms':total_rooms,'available':available,'unavailable':unavailable}
    return render(request,'me/panel.html',context)
    
    
 
def other(request):
    return render(request,'me/panel.html')
@login_required(login_url='/login/')
def edit_room(request):
    
    if request.method == 'POST':
       
        old_room = Living()
       # old_room.room_type  = request.POST['roomtype']
        old_room.capacity   =(request.POST['capacity'])
        old_room.price      = (request.POST['price'])
        old_room.size       = (request.POST['size'])
        old_room.room_type       = (request.POST['room_type'])
        old_room.status       = (request.POST['status'])
        total_rooms = len(Living.objects.all())
        
       
        old_room.roomnumber = total_rooms + 1
        old_room.save()
        
       
        messages.success(request,"Room Details Updated Successfully")
        return render(request,'me/index.html')
    else:
    
        room_id = request.GET['id']
        print(room_id)
        room = Living.objects.all().get(id=room_id)
        response = render(request,'me/editroom.html')
        return HttpResponse(response)

#for adding room
@login_required(login_url='/login')
def add_new_room(request):

    if request.method == "POST":
        total_rooms = len(Living.objects.all())
        new_room = Living()
      

        new_room.roomnumber = total_rooms + 1
        new_room.room_type  = request.POST['roomtype']
        new_room.capacity   = (request.POST['capacity'])
        new_room.size       = (request.POST['size'])
        new_room.status     = request.POST['status']
        new_room.price      = request.POST['price']
        

        new_room.save()
        messages.success(request,"New Room Added Successfully")
    
    return redirect('panel')

#booking room page
@login_required(login_url='/login/')
def book_room(request):
    room = Living.objects.all().get(id=int(request.GET['roomid']))
    return HttpResponse(render(request,'me/room.html'))

#For booking the room
@login_required(login_url='/login/')
def book_roomm(request):
    
    if request.method =="POST":

        room_id = request.POST['room_id']
        
        room = Living.objects.all().get(id=room_id)
        #for finding the reserved rooms on this time period for excluding from the query set
        for each_reservation in Reservation.objects.all().filter(room = room):
            if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(request.POST['check_out']):
                pass
            elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(each_reservation.check_out) > str(request.POST['check_out']):
                pass
            else:
                messages.warning(request,"Sorry This Room is unavailable for Booking")
                return redirect("homepage")
            
        current_user = request.user
        total_person = int( request.POST['person'])
        booking_id = str(room_id) + str(datetime.datetime.now())

        reservation = Reservation()
        room_object = Rooms.objects.all().get(id=room_id)
        room_object.status = '2'
        
        user_object = User.objects.all().get(username=current_user)

        reservation.guest = user_object
        reservation.room = room_object
        person = total_person
        reservation.check_in = request.POST['check_in']
        reservation.check_out = request.POST['check_out']

        reservation.save()

        messages.success(request,"Congratulations! Booking Successfull")

        return redirect("index.html")
    else:
        return HttpResponse('Access Denied')

   
def dell(request,roomnumber):
   

       
        
    living=Living.objects.all().get(roomnumber=roomnumber)
    living.delete()
    context={}
    context['roomnumber']=roomnumber
    
    return render(request,"panel.html",context)
    
def get_queryset(request):

    
    return Living.objects.all()

def delete(request):


    if request.method=="POST":

        roomnumber=request.POST["rd"]
        context={}
        context['roomnumber']=roomnumber
        living=Living.objects.all().get(roomnumber=roomnumber)
        living.delete()
        messages.success(request,f'Deleted successfully!')
        

       
        return render(request,"me/delete.html",context)
    else:

        messages.success(request,f'Enter valid roomnumber')

   
    return render(request,"me/delete.html")
     
    
       


   
    
    

