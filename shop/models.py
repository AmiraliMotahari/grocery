from django.db import models
from django.urls import reverse

# Create your models here.

class ProductVariation(models.Model):
    name = models.CharField(max_length=200, verbose_name="Category Name")
    
    def __str__(self): 
        return self.name
    
    def get_absolute_url(self): # 
        return reverse('productVariationList')



class City(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    
    def __str__(self): 
        return self.name
    
    def get_absolute_url(self): # 
        return reverse('cityList')

    
class Inventory(models.Model):
    cityId = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City")
    
    def __str__(self):
        return self.cityId.name
    
    def get_absolute_url(self): 
        return reverse('inventoryList')
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(verbose_name="Quantity in Kg")
    pType = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, verbose_name="Category Name")
    cityId = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City Name")
    
    def __str__(self): 
        return self.name
    
    def get_absolute_url(self): # 
        return reverse('productList')

 
    
class InventoryProduct(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product Name")
    inventoryId = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name="Inventory City")
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.productId.name
    
    def get_absolute_url(self): # 
        return reverse('inventoryProductList')
 
    
class Supplier(models.Model):
    firstName = models.CharField(max_length=50, default='')
    LastName = models.CharField(max_length=50, default='')
    phoneNum = models.CharField(null=False, blank=False, default="", unique=True, max_length=50)
    email = models.EmailField(default='')
    address = models.CharField(max_length=200, default='')
    
    def __str__(self): 
        return self.LastName
    
    def get_absolute_url(self): 
        return reverse('supplierList')
 
    
from accounts.models import CustomUser   
    
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default='')
    product = models.ForeignKey(InventoryProduct, on_delete=models.CASCADE,default='')
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0)
    
    SUBMITTED = 'submitted'
    READY_TO_SEND = 'ready to send'
    STATUS_CHOICES = [(SUBMITTED, 'submitted'),
        (READY_TO_SEND, 'ready to send'),]
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=SUBMITTED)
  
    def __str__(self):
        return str ('{name} ({prod} * {quan})'.format(name=self.user.username, prod=self.product, quan=self.quantity))
    
    # def get_absolute_url(self): 
    #     return reverse('AdminOrderList')
    
    
    #   return self.user.first_name
    

    
        
     