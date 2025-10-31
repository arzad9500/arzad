from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage),
    path('base/',base),
    path('navebar/',navebar),
    # path('product_add/',product_add), # 6 form page
    # path('allproduct/',allproduct),
    # path('delete_product/<int:id>',delete_product,name='del_pro'),
    # path('update_product/<int:id>',update_product,name='upd_pro'),

    path('product_add/',productaddview.as_view()), # class base view
    path('allproduct/',productallview.as_view()),
    path('delete_product/<int:id>',productdeleteview.as_view(),name='del_pro'),
    path('update_product/<int:id>',productupdateview.as_view(),name='upd_pro'),
 
]