from django.urls import path
from .views import *


urlpatterns = [
    path('addcustomer/',addcustomer),
    path('allcustomer/',allcustomer),
    path('deletecustomer/<int:id>',deletecustomer,name='del_cust'),
    path('updatecustomer/<int:id>',updatecustomer,name='upd_cust'),


    path('addorders/',addorders),
    path('allorders/',allorders),

    path('deleteorders/<int:id>',deleteorders,name='del_ord'),
    path('updateorders/<int:id>',updateorders,name='upd_ord'),
]