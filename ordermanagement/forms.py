from django import forms
from django.forms import ModelForm
from .models import *

class customer_form (ModelForm):

    class Meta:
        model = customer
        fields = '__all__'


class orders_form(ModelForm):

    class Meta:
        model=orders
        fields = ['customer_reference','product_reference','order_number','order_date','quantity'] 
        # we put only some fields because total amount is differ by every quantity , we calculate manually in views.py
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date','id': 'order_date',})
        } # to show date picker in order date field like  html date input type