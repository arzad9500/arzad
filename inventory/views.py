from django.shortcuts import render,redirect
from .models import *    # this and down for product_add function
from .forms import *
from django.contrib.auth.decorators import login_required  # this for function based view

from django .views import View  # this for class based function
from django.contrib.auth.mixins import LoginRequiredMixin # this type for class based view

@login_required(login_url='/')  # this for function based view
def homepage (request):

    data  = {
        'name' : 'arzad',
        'list': [1,2,3,4],
        'mark' :{
            'tamil': 55,
            'english' : 65,
            'maths' :  66,
            'science' : 75,
            'social' : 73,
        }   
    }
    return render(request,'home.html',data)

@login_required(login_url='/')  # this for function based view
def base(request):
    return render (request,'base.html')

@login_required(login_url='/')  # this for function based view
def navebar(request):
    return render (request,'navebar.html')

def product_add(request):   # 4 this function for to show forms.py in ---> # 5 product_add.html(ui) page and collect the data 

    data  ={
        'p_form' : product_form()  # 4  # product_form is from forms.py 
    }                                   # p_form  is we will used in product_add.html

    if request.method == 'POST' :  # 7    # if we collect data from ui and save in db down 3 line
        pr_form = product_form(request.POST) # 
        # print(request.POST)

        if pr_form.is_valid():
            pr_form.save()

            return redirect('/inventory/allproduct/')  # after save redirect to allproduct page

    return render (request,'product_add.html',data)  # 4

def allproduct(request): # 8 to show d/b content in ---> # 9 allproduct.html (ui)# 

    data ={
        'all_p' : product.objects.all()  #  this product is model name # objects is field
    }
    return render (request,'allproduct.html',data)

def delete_product(request,id): # 11 # every function need url, # 12 next url next allproduct.html button href

    dele = product.objects.get(id = id)
    dele.delete()

    return redirect('/inventory/allproduct/') # delete and redirect to same page

def update_product(request,id): # 13 # 13 is prefield data and load in product_add.html(form) page
    update = product.objects.get(id = id) # 13 # this and down two just get the instance and create url
    data =  {
        'p_form' : product_form(instance=update) # 13 #  we already choose p_form name in up product_add function and the same name we use in product_add.html so dont change this name 
        } # product_form is from forms.py
    
    if request.method=='POST': # 14 #  this if and this return prefield take data and go to form html page ('product_add.html')
            pro_form = product_form(request.POST,instance=update) # if dont pass this --> instance=update this will add new data 
            if pro_form.is_valid():  # this and this return in form page with data and
                pro_form.save()    # update the value in form and down 

                return redirect('/inventory/allproduct/')  # up done and this is redirect to allproduct.html page

    return render(request,'product_add.html',data) # 13  # we touch update button the data go to 'product_add.html' (form) page 




class productaddview(LoginRequiredMixin,View): # login_required is first

    login_url='/'

    def get (self,request): # take data from backend to frontend (http) 
        # print('from class base get') 
        data  = {
        'p_form' : product_form()   
        }

        return render (request,'product_add.html',data)  
    
    def post(self,request): # take data from frontend to backend  (https) 
        # print('from class base get')
        pr_form =product_form(request.POST,request.FILES) # request.FILES for image input

        if pr_form.is_valid():
            pr_form.save()

            return redirect('/inventory/allproduct/')

class productallview(LoginRequiredMixin,View):

    login_url='/'

    def get(self,request):
        data ={
        'all_p' : product.objects.all()  #  this product is model name # objects is filed
        }
        return render (request,'allproduct.html',data)

class productdeleteview(LoginRequiredMixin,View):
    
    login_url='/'

    def get(self,request,id):
        dele = product.objects.get(id = id)
        dele.delete()
        return redirect('/inventory/allproduct/') # delete and redirect to same page

class productupdateview(LoginRequiredMixin,View):
    
    login_url='/'

    def get(self,request,id):
        update = product.objects.get(id = id) # 13 # this and down two just get the instance and create url
        data =  {
            'p_form' : product_form(instance=update) # 13 #  we already choose p_form name in up product_add function and the same name we use in product_add.html so dont change this name 
            } # product_form is from forms.py
        return render(request,'product_add.html',data) # 13  # we touch update button the data go to 'product_add.html' (form) page 

    def post(self,request,id):
            update = product.objects.get(id = id) # 13 # this and down two just get the instance and create url
            pro_form = product_form(request.POST,instance=update) # if dont pass this --> instance=update this will add new data 

            if pro_form.is_valid():  # this and this return in form page with data and
                pro_form.save()    # update the value in form and down 

                return redirect('/inventory/allproduct/')
            


      

 
     

