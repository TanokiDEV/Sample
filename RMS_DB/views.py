from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *

from .forms import EmployeeForm 
from .models import Employee
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import OrderForm, CreateUserForm
from .forms import CustomerForm
from .filters import OrderFilter

from .forms import ProductForm


from .decorators import unauthenticated_user, allowed_users

@unauthenticated_user
def registerPage(request):
       
    form = CreateUserForm()
    if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user )
            
                return redirect('login')
    
    context = {'form':form}
    return render(request,"design/registerPage.html", context)

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
                login(request, user)
                return redirect('menu')
        else:
            messages.info(request, 'Username or Password is incorrect')
            
    context = {}
    return render(request,"design/loginPage.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')


###########################################################################
@login_required(login_url='login')
def employee_confirm(request):
    
    return render(request,"design/employee_confirm.html",)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,"design/employee_list.html",context)

@login_required(login_url='login')
def employee_list2_user(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,"design/employee_list2_user.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employee_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"design/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('menu')
      
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('menu')

############################################################
@login_required(login_url='login')

def menuPage(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    
    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    out_for_delivery = orders.filter(status='Out For Delivery').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'delivered':delivered,
    'out_for_delivery':out_for_delivery,
    'pending':pending}
    
    return render(request,"design/menuPage.html", context)


@login_required(login_url='login')
def products_view(request):
    products = Product.objects.all()
    return render(request, 'design/products_view.html', {'products': products})

@login_required(login_url='login')
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    
    
    orders= customer.order_set.all()
    order_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    context = {'customer':customer, 'orders':orders, 'order_count':order_count,
    'myFilter':myFilter} 
    return render(request, 'design/customer.html',context)

######################################################################

@login_required(login_url='login')
def createOrder(request, pk):
    
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    
    if request.method == 'POST' :
        #print('Printing POST:', request.POST)
        form= OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
        
    context = {'form':form}
    return render(request, 'design/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    
    order = Order.objects.get(id=pk)
    form= OrderForm(instance=order)
    
    if request.method == 'POST' :
        form= OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('menu')
    
    context = {'form':form}
    return render(request, 'design/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method =="POST":
        order.delete()
        return redirect('menu')
    
    context = {'item':order}
    return render(request, 'design/delete_order.html', context)

################################################

@login_required(login_url='login')
def createCustomer(request, id=0):
    if request.method == "GET":
        if id==0:
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(request,"design/customer_form.html",{'form':form})
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST,instance= customer)
        if form.is_valid():
            form.save()
        return redirect('menu')
    
@login_required(login_url='login')   
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form= CustomerForm(instance=customer)
    
    if request.method == 'POST' :
        form= CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('menu')
    
    context = {'form':form}
    return render(request, 'design/customer_form.html', context)


@login_required(login_url='login')
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method =="POST":
        customer.delete()
        return redirect('menu')
    
    context = {'customer':customer}
    return render(request, 'design/delete_customer.html', context)

##################################################################

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    
    
    return render(request, 'design/products.html', {'products': products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createProduct(request, id=0):
   
    if request.method == "GET":
        if id==0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(request,"design/products_form.html",{'form':form})
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product= Product.objects.get(pk=id)
            form = ProductForm(request.POST,instance= product)
        if form.is_valid():
            form.save()
        return redirect('products')
    
    

    
