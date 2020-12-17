from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employee

from django.forms import ModelForm, fields
from .models import Order
from .models import Customer

from .models import Tag
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
	        
  

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email')
        

    def __init__(self, *args, **kwargs):
        super(CustomerForm,self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['phone'].required = False
    
class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('fullname','age','gender','email','mobile','emp_code','position')
        labels = {
            
            'fullname': 'Full Name',
            'age': 'Age',
            'gender': 'Gender',
            'email': 'Email',
            'mobile': 'Mobile Number',
            'emp_code':'Employee Code',
            'position': 'Position',
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = True
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']