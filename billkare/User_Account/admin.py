from django.contrib import admin
from .models import SLTAuth,SLTLogin,SLT_accesstocken


# Register your models here.

# class BanknameAdmin(admin.ModelAdmin):
    # list_display=('bank_choices')    

admin.site.register(SLTAuth)
admin.site.register(SLTLogin)
admin.site.register(SLT_accesstocken)


#admin username:admin@gmail.com
#password :admin