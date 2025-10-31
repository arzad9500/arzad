from django.db import models
from django.contrib.auth.models import AbstractUser # 1

# this model is custom user defined model and project settings line 134
class user(AbstractUser): # user is custom model and AbstractUser is joind with our fields
    
    age = models.IntegerField(default=0) # this field is add with default 

    role_choices =  (
        (0, 'Admin'),
        (1, 'Manager'),
        (2, 'Employee'),
        )
    
    role = models.IntegerField(default=0,choices=role_choices)


