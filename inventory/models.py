from django.db import models

# Create your models here.
class product(models.Model): # 1 # add this fiels to database # 2 admim.py
    product_name = models.CharField( max_length=200,null=True)
    product_code = models.CharField(max_length=200,null=True)
    price = models.FloatField (default = 0)
    gst = models.IntegerField(default = 0)
    food_product = models.BooleanField(default=False)
    picture =models.ImageField(null=True,blank=True,upload_to='imag/') # this imag is inside of static files
    # Database allows ( NULL = true )
    #Form validation allows no image uploaded ( blank=True ,ui)
# need pillow package for user image input
    def __str__(self): # return string
        return self.product_name + ' ' + self.product_code # this two will show in orders dropdown
