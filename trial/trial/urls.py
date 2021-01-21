"""trial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from me import views as me_view

from django.contrib.auth import views as auth
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('me/',include('me.urls')),
    path('login/',me_view.acess,name="login"),
    path('hotel/',me_view.hotel,name='hotel'),
    path('room/',me_view.hotel,name='room'),
    path('panel/me/editroom/',me_view.edit_room,name='panel/me/editroom'),
   
    path('panel/me/delete/delete/',me_view.dell,name='panel/me/delete/delete'),
    path('panel/me/delete/delete/<int:roomnumber>/panel.html/',me_view.Liviing.as_view(),name='panel/me/delete/delete'),
    #re_path(r'^panel/delete/(?P<id>[0-9]+)/$',me_view.dell),
    path('delete/<int:roomnumber>',me_view.dell,name='delete'),
   
    path('panel/me/delete/',me_view.delete,name='panel/me/delete'),
    
   
    path('edit_room/',me_view.edit_room,name='edit_room'),
    path('panel/',me_view.Liviing.as_view(),name='panel'),
    path('getu/',me_view.getu,name='getu'),
    path('delete/',me_view.delete,name='delete'),
    path('live/',me_view.other,name='live'),
    path('acess/',me_view.acess,name='acess'),
    path('logout/',auth.LogoutView.as_view(template_name='me/index.html'),name="logout"),
    path('admin/', admin.site.urls),
    path('Menu/',me_view.Menulist.as_view() ,name="Menu"),
    path('book/',me_view.bookView,name="book"),
    path('good/',me_view.booksub,name="good"),
    path('add_new_room/',me_view.add_new_room,name="add_new_room"),
    path('index/',me_view.index,name="index"),
    path('menu/',me_view.menu,name="menu"),
    path('about/',me_view.about,name="about"),
    path('well/',me_view.well,name="well"),
    path('msg/',me_view.emailsending,name="msg"),
    #path('Email',include['me.urls']),
]
