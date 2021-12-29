from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):

   fields =('first_name','last_name','email','number','gender')

   radio_fields = {'role': admin.VERTICAL}
