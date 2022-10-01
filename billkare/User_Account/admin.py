from django.contrib import admin
from .models import User,login_history


# Register your models here.

# class BanknameAdmin(admin.ModelAdmin):
    # list_display=('bank_choices')    

admin.site.register(User)
admin.site.register(login_history)



#admin username:admin@gmail.com
#password :admin