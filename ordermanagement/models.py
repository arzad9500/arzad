from django.db import models
from inventory.models import * # we use inventory model inside orders model

# Create your models here.
class customer(models.Model):
    customer_name = models.CharField(max_length=200,null=True)
    customer_since = models.DateField(null=True)

    def __str__ (self):
        return self.customer_name 
# + ' ' +  str(self.customer_since)
    

class orders(models.Model): # down line ForeignKey fiels stores in d/b  with --> customer_reference_id
    customer_reference = models.ForeignKey(customer, on_delete=models.CASCADE, null=True) # when we delete customer , the  order for the customer is automatic delete
    product_reference = models.ForeignKey(product, on_delete=models.SET_NULL, null=True) # when order is delete , this will take null 
    order_number = models.CharField(max_length=20, null=True)
    order_date = models.DateField(null=True)
    quantity = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    bill_amount = models.FloatField (default=0)

    def __str__(self):
        return self.order_number
