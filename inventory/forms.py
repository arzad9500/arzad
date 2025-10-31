# we need take input from UI so this form is 1st , and in views la 1st 2 line 
# and product_add.html la and url 
from django.forms import ModelForm, NumberInput, CheckboxInput, FileInput
from django import forms
from .models import *

class product_form(ModelForm): # 3 this forms for models ,to show models fields in ui # 4 views.py

    class Meta:

        model = product      # this product is models  # then go to 
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control product_name'}),
            'product_code': forms.TextInput(attrs={'class': 'form-control product_code'}),
            'price': forms.NumberInput(attrs={'class': 'form-control price'}),
            'gst': forms.NumberInput(attrs={'class': 'form-control gst'}),
            'food_product': forms.CheckboxInput(attrs={'class': 'form-check-input food_product'}),
            'picture': forms.FileInput(attrs={'class': 'form-control picture'}),
        } # file input for image field and need enctype='multipart/form-data , and  pillow  package , request.FILES in views.py


