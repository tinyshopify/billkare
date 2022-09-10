

import logging
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator



numeric = RegexValidator(r'^(\+\d{1,3})?,?\s?\d{8,13}', 'ENTER VAILD PHONE NUMBER.')



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        

        user = self.model(
            email=self.normalize_email(email)
        )
      
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email,password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        

        user = self.model(
            email=self.normalize_email(email)
        )
        
        user.set_password(password)
      
        user.admin = True
        user.staff = True
        user.active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

# class BANKCHOICES(models.Model):

#         bank_choices=models.CharField(max_length=50,verbose_name='choices')
        
#         def __str__(self):
#          return self.bank_choices
         
#         @staticmethod
#         def getbankname( bankid):
#           return BANKCHOICES.objects.filter (id=bankid)
         



class SLTAuth(AbstractBaseUser):
    # sal_bname       = models.CharField(max_length=50,blank=True)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
   
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=30,validators=[numeric])
    sourcelantics_id=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
   
 
    def __str__(self):
        return self.email
    
       
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    
class SLTLogin(models.Model):
    user_email=models.EmailField(max_length=100)
    last_login      = models.DateTimeField(auto_now_add=True)
    # salary_bankname=models.CharField(max_length=50)
   
   
class SLT_accesstocken(models.Model):
     SLT_id= models.ForeignKey(SLTAuth,on_delete=models.CASCADE,default=uuid.uuid4 )
     access_token=models.CharField(max_length=50,blank=True)



  