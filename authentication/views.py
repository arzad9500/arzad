from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth  import authenticate , login , logout # 5
from .models import user
from django.contrib.auth.decorators import login_required 

# 1 
def loginpage(request):# 1  # check YT 22 la 6.00
    # if we login once , we no need to login again and again until we logout
    if request.user.is_authenticated: # user is from down     # this and downn for automatic login , 
        return redirect('/inventory/allproduct/') # if authentication this will redrect
    # user is authenticated(session) then he go without logout this happen
    context ={  # 10
        'error':''
    }

    if request.method == 'POST':# 3 when we submit the login form that is POST  
        print(request.POST)# 4  # this from ui username and password and print in therminal 

        user =  authenticate(username=request.POST['u_name'], password=request.POST['p_word'])# 5 # username and password is keyword and u_name is form(login.html) name 
        print(user)# 6 # create superuser before this # think # this check superuser and not valid superuser it will return none then next line

        if user is not None:# 7 # that mean superuser is match
            login(request,user)# 8 # it will create login session # then redirect to down page

            return redirect('/order/allcustomer/')# 9 
        
        else :# 11 # when username and password not match this happen
            context ={
                'error':' *invalid username or password'
            }
            return render (request,'login.html',context) # redirect to same login page

    return render (request,'login.html',context)# 2

@login_required(login_url='/') # these for if we login we access this page (cannot access through url by manual)
def  logoutpage(request): # 
    logout (request)   # request already store user(this happen in login inside if) so we pass only the request 

    return redirect ('/')

# @login_required(login_url='/')
def signuppage(request):           # @   check YT 23 video
     
     context ={
            'error' : '',
            'data'  : {}   # 👈 empty dict  when we first open signup
        }
     
     if request.method == 'POST': # @ 
        # Store posted data temporarily
        entered_data = { # we use this for redirect and show entered data in ui when error occur (matched user name found)
            'f_name': request.POST.get('f_name', ''),  # we use this in ui 
            'lastname': request.POST.get('lastname', ''),
            'u_name': request.POST.get('u_name', ''),
            'e_mail': request.POST.get('e_mail', ''),
            'age': request.POST.get('age', ''),
            'role': request.POST.get('role', ''),
        }

        user_check = user.objects.filter(username = request.POST['u_name'] ) # 2 # if same username is available ret
        # print(user_check)  # if username is already available shows in -->[mohamed] else -->[]

        if len(user_check) > 0 : # 2 # if matching data is available it work , else go to else part
            context = {  # 2
                'error' : ' * username is already exists plz.. use another username',
                'data'  : entered_data   # 👈 pass back user data
            } 

            return render(request, 'signup.html',context)

        else : # user is model 
            new_user = user(  # @  # 2 is come inside of else part
            first_name=request.POST['f_name'], # @  # first_name is from d/b name , f_name is from ui (signup.html) 
            last_name=request.POST['lastname'], # @ 
            username=request.POST['u_name'], # @ 
            email=request.POST['e_mail'], # @ 
            age=request.POST['age'], # @ 
            role=request.POST['role'], # @
            )
            new_user.set_password(request.POST['p_word']) # @ 
            new_user.save() # @ 

            logout(request) # @  #  logout any user is login
            
            return redirect('/')  # @ new signup is done so redirect to login page

     return render(request, 'signup.html',context)
