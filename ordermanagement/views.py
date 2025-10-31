from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required # this works only function based view

@login_required(login_url='/') # this for login required 
def addcustomer(request):   # after add customer make this page auto redirect

    data  ={
        'c_form' : customer_form()      # 
    }                              # 
    if request.method == 'POST' :   # 
        cs_form =customer_form(request.POST)

        if cs_form.is_valid():
            cs_form.save()
    
    return render(request,'addcustomer.html',data)

@login_required(login_url='/')
def allcustomer(request):
    data = {
        'all_cust' : customer.objects.all()
    }
    return render(request,'allcustomer1.html',data)

@login_required(login_url='/')
def deletecustomer(request,id):

    del_pro=customer.objects.get(id=id)
    del_pro.delete()

    return redirect('/order/allcustomer/')

@login_required(login_url='/')
def updatecustomer(request,id):
    update = customer.objects.get(id = id) # 

    data =  {
        'c_form' : customer_form(instance=update) #   
        }
        
    if request.method=='POST':  # 
          cust_form = customer_form(request.POST,instance=update) 

          if cust_form.is_valid(): # this and this return in form page with data and
            cust_form.save()    # update the value in form and down 

            return redirect('/order/allcustomer/')

    return render(request,'addcustomer.html',data)


@login_required(login_url='/')
def addorders(request):

    data ={
        'ord_form' : orders_form()  # orders_form is from forms
    }
    if request.method == 'POST': #  check code camp 17 th video 
        # print(request.POST) # take input drom ui and check in terminal
        selected_product = product.objects.get(id = request.POST['product_reference']) #  post method quantity and price will change so use product_reference 
        # take throuugh id and get all value of product
        amount = float(selected_product.price) * float(request.POST['quantity']) # amount is price its in inventory

        gst_amount= (amount * selected_product.gst) / 100 # selected_product stores all the value of product_reference

        bill_amount = amount + gst_amount
        
        # we post this is manual method # because we need calculate amount (quantity by differ)
        new_order = orders(customer_reference_id = request.POST['customer_reference'],
                            product_reference_id = request.POST['product_reference'], order_number = request.POST
                            ['order_number'], order_date = request.POST['order_date'], quantity = request.POST
                            ['quantity'], amount = amount, gst_amount = gst_amount, bill_amount = bill_amount)
        new_order.save() # customer_reference_id these 1st name is all from d/b name (because foreign key model is _id is add)

        return redirect('/order/allorders/') #  after new order this page is redirect to allorder page

    return render (request,'addorders.html',data)

@login_required(login_url='/')
def allorders(request):
    data={
        'all_ord':orders.objects.all()  # all_ord we use in --> allorders.html page in table format
    }
    return render (request,'allorders.html',data)

@login_required(login_url='/')
def deleteorders(request,id):

    del_ord=orders.objects.get(id=id)
    del_ord.delete()

    return redirect('/order/allorders/')

@login_required(login_url='/')
def updateorders(request,id):
    upd_ord=orders.objects.get(id=id)

    data ={
        'ord_form' : orders_form(instance=upd_ord) # prefield the data and go in --> orders_form(addorder) 
    }

    if request.method == 'POST': # in update we change somethinng so up logic will apply down 4 line
        # print(request.POST)
        selected_product = product.objects.get(id = request.POST['product_reference'])

        amount = float(selected_product.price) * float(request.POST['quantity']) # amount is price its in inventory

        gst_amount= (amount * selected_product.gst) / 100

        bill_amount = amount + gst_amount

        filter_order = orders.objects.filter(id=id) # new check YT 18 video 16.00
        filter_order.update(customer_reference_id = request.POST['customer_reference'],
                            product_reference_id = request.POST['product_reference'], order_number = request.POST
                            ['order_number'], order_date = request.POST['order_date'], quantity = request.POST
                            ['quantity'], amount = amount, gst_amount = gst_amount, bill_amount = bill_amount)


        return redirect('/order/allorders/') #  this page is redirect to allorder page

    return render(request,'addorders.html',data)
 


