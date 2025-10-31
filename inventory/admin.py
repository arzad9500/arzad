# we create superuser that for acess admit page 

from django.contrib import admin

from .models import * # 2 # this for show models.py in admin page and access (add, delete)# 3 forms.py

admin.site.register(product) # product is models name 

