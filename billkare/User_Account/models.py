

import datetime

from django.db import models
from django.utils.timezone import now
import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator





numeric = RegexValidator(r'^(\+\d{1,3})?,?\s?\d{8,13}$', message="Phone number must be entered in the format:'+99999'.upto 15 digits allowed.")
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible

# @deconstructible
# class WhitelistEmailValidator(EmailValidator):

#     def validate_domain_part(self, domain_part):
#         return False

#     def __eq__(self, other):
#         return isinstance(other, WhitelistEmailValidator) and super().__eq__(other)


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


class TimeStampModel(models.Model):
    isActive        = models.BooleanField(default=True,db_index=True)
    creUser         =models.CharField(max_length=50,default=None,db_index=True)
    CreatedTs       =models.DateTimeField(null=True,db_index=True)
    UpdateTs        =models.DateTimeField(null=True,db_index=True)
    creDate         =models.DateTimeField(auto_now_add=True,null=True,db_index=True)
    InsUpdFlag      =models.CharField(max_length=50,null=True,db_index=True)
   

    class Meta:
        abstract = True
      


class User(AbstractBaseUser,TimeStampModel):
  
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    # email           = models.EmailField(max_length=100, unique=True,validators=[WhitelistEmailValidator(whitelist=['gmail.com', 'yahoo.com', 'hotmail.com'])])
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=15,unique=True,validators=[numeric])
    Sugan_id         =models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
    CreatedDate    = models.DateTimeField(auto_now_add=True)
 
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
  
class current_login(TimeStampModel):
    Eventid=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
    Sugan_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    user_email      =models.EmailField(max_length=100)
    last_login      = models.DateTimeField(auto_now_add=True)
    log_outtime     =models.DateTimeField(null=True,blank=True)
       
class login_history(TimeStampModel):
    Eventid=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
    Sugan_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    user_email      =models.EmailField(max_length=100)
    last_login      = models.DateTimeField(auto_now_add=True)
    log_outtime     =models.DateTimeField(null=True,blank=True)
   
class Sugan_wishlist(TimeStampModel):
    Eventid=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
    email=models.EmailField(max_length=100,null=True,blank=True,unique=True)


  