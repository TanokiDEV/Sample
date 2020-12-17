from django.db import models


class Position(models.Model):
   title = models.CharField(max_length=50)
    
   def __str__(self):
        return self.title
     
class Gender(models.Model):
   sex = models.CharField(max_length=6)
   
   def __str__(self):
        return self.sex
     
class Employee(models.Model):
   fullname = models.CharField(max_length=100)
   emp_code = models.CharField(max_length=4)
   gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
   age = models.CharField(max_length=2)
   email = models.CharField(max_length=30)
   mobile = models.CharField(max_length=11)
   date_created = models.DateTimeField(auto_now_add=True)
   position = models.ForeignKey(Position,on_delete=models.CASCADE)
   
####################################

class Customer(models.Model):
   name = models.CharField(max_length=200, null=True)
   phone = models.CharField(max_length=11, null=True)
   email = models.CharField(max_length=200, null=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True)

   def __str__(self):
         return self.name
      
      
class Tag(models.Model):
   name = models.CharField(max_length=200, null=True)
  
   def __str__(self):
         return self.name

   
class Product(models.Model):
   CATEGORY = (
            ('Bread', 'Bread'),
            ('Vegetables', 'Vegetables'),
            ('Meat', 'Meat'),
            ('Fish', 'Fish'),
            )
   name = models.CharField(max_length=200, null=True)
   price = models.FloatField(null=True)
   category = models.CharField(max_length=200, null=True, choices=CATEGORY)
   description = models.CharField(max_length=200, null=True, blank=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True)
   tag = models.ForeignKey(Tag, null=True, on_delete= models.SET_NULL)
   
   def __str__(self):
         return self.tag
  
   def __str__(self):
         return self.name
   

class Order(models.Model):
   STATUS = (
            ('Pending', 'Pending'),
            ('Out For Delivery', 'Out For Delivery'),
            ('Delivered', 'Delivered'),
            )
   customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
   product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
   date_created = models.DateTimeField(auto_now_add=True, null=True)
   status = models.CharField(max_length=200, null=True, choices=STATUS)
  
   
   def __str__(self):
         return self.product.name

