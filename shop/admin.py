from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(City)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(ProductVariation)
admin.site.register(InventoryProduct)
admin.site.register(Supplier)