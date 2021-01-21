from django.contrib import admin
admin.site.site_header="welcome"
admin.site.index_title="good day"
admin.site.site_title="good"
# Register your models here.
from .models import Login,register,Menu,Boopay,Hotel,Living,Reservation

admin.site.register(Login)
admin.site.register(register)
admin.site.register(Menu)
admin.site.register(Boopay)
admin.site.register(Hotel)
admin.site.register(Living)
admin.site.register(Reservation)

#class BoopayInline(admin.TabularInline):
     #(model=Boopay

#class registeradmin(admin.ModelAdmin):
    #fieldsets=[('Name',{'fields':['name']}),
    #('address',{'fields':['address']}),
     #(('age',{'fields':['age']}),
     #(('email',{'ields':['email']}),
     #(('phone',{'fields':['phone_no']}),
     #(('state',{'fields':['state']}),
    #( ]
    #( inlines=[BoopayInline]
#admin.site.register(register,registeradmin)

