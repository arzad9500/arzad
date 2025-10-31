from django.urls import path,include
from .views import *

urlpatterns = [
    path('',loginpage),
    path('logoutpage/',logoutpage),
    path('signuppage/',signuppage),
]
