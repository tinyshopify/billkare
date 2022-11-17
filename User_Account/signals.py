from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

 
 

@receiver(post_save, sender=User)
# def create_signup(sender, instance, created, **kwargs):
#     print("User created")
  
@receiver(post_save, sender=User)
def save_signup(sender, instance, **kwargs):
        print("User created")
