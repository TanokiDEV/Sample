from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'), #user register 
    path('logout/', views.logoutUser, name='logout'),
    
    path('form/', views.employee_form, name='form'),# get and post req. for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.employee_delete, name='employee_delete'), # delete employee operation
    path('list/', views.employee_list, name='employee_list'), # get req. to retrive and display all records. # for admin creator only
    path('confirm/', views.employee_confirm, name='employee_confirm'),
    path('list2/', views.employee_list2_user, name='employee_list2_user'),
    
    
   
    
   
    path('menu/', views.menuPage, name='menu'),
    path('products_view/', views.products_view, name='products_view'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    
    
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"),
    
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    
    path('create_product/', views.createProduct, name="create_product"),
    
]

   
   




