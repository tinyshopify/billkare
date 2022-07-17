from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# SuperUserInformation
# User: admin
# Email: nandhini@gmail.com 
# Password: 1234567

numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')
# Create your models here.
class customer_Info(models.Model):

    # Create relationship 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    customer_phonenumber=models.CharField("Phone Number :", max_length=30,validators=[numeric])

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
        
    def get_user(self, user_id):
        return User.objects.get(pk=user_id)