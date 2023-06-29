from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView, DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django import forms
   
    
#admin pages
class AdminPage(TemplateView, LoginRequiredMixin):
    template_name = 'adminHome.html'  
    
class CityCreateView(CreateView):
    model = City
    template_name = 'cityCreate.html'
    fields = ['name']
    
# class CityDetailView(DetailView):
#     model = City
#     template_name = 'forms_create.html'
    
class CityListView(ListView,LoginRequiredMixin):
    model = City
    template_name = 'cityList.html'
    
class CityUpdateView(UpdateView,LoginRequiredMixin):
    model = City
    template_name = 'cityUpdate.html'
    fields = ['name']
    
class CityDeleteView(DeleteView,LoginRequiredMixin):
    model = City
    template_name = 'cityDelete.html'
    fields = ['name']
    success_url = reverse_lazy('cityList')
    
    
    
    
    
class ProductCreateView(CreateView,LoginRequiredMixin):
    model = Product
    template_name = 'productCreate.html'
    fields = ['name','price', 'quantity', 'pType', 'cityId']
    
class ProductListView(ListView,LoginRequiredMixin):
    model = Product
    template_name = 'productList.html'
    
class ProductUpdateView(UpdateView,LoginRequiredMixin):
    model = Product
    template_name = 'productUpdate.html'
    fields = ['name','price', 'quantity', 'pType', 'cityId']
    
class ProductDeleteView(DeleteView,LoginRequiredMixin):
    model = Product
    template_name = 'productDelete.html'
    fields = ['name','price', 'quantity', 'pType', 'cityId']
    success_url = reverse_lazy('productList')



class ProductVariationCreateView(CreateView,LoginRequiredMixin):
    model = ProductVariation
    template_name = 'productVariationCreate.html'
    fields = ['name']
    
class ProductVariationListView(ListView,LoginRequiredMixin):
    model = ProductVariation
    template_name = 'productVariationList.html'
    
class ProductVariationUpdateView(UpdateView,LoginRequiredMixin):
    model = ProductVariation
    template_name = 'productVariationUpdate.html'
    fields = ['name']
    
class ProductVariationDeleteView(DeleteView,LoginRequiredMixin):
    model = ProductVariation
    template_name = 'productVariationDelete.html'
    fields = ['name']
    success_url = reverse_lazy('productVariationList')

    
class SupplierCreateView(CreateView,LoginRequiredMixin):
    model = Supplier
    template_name = 'supplierCreate.html'
    fields = "__all__"
    
class SupplierListView(ListView,LoginRequiredMixin):
    model = Supplier
    template_name = 'supplierList.html'
    
class SupplierUpdateView(UpdateView,LoginRequiredMixin):
    model = Supplier
    template_name = 'supplierUpdate.html'
    fields = "__all__"
    
class SupplierDeleteView(DeleteView,LoginRequiredMixin):
    model = Supplier
    template_name = 'supplierDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('supplierList')
    
    
class InventoryCreateView(CreateView,LoginRequiredMixin):
    model = Inventory
    template_name = 'inventoryCreate.html'
    fields = "__all__"
    
class InventoryListView(ListView,LoginRequiredMixin):
    model = Inventory
    template_name = 'inventoryList.html'
    
class InventoryUpdateView(UpdateView,LoginRequiredMixin):
    model = Inventory
    template_name = 'inventoryUpdate.html'
    fields = "__all__"
    
class InventoryDeleteView(DeleteView,LoginRequiredMixin):
    model = Inventory
    template_name = 'inventoryDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('inventoryList')
    
    
    
class InventoryProductCreateView(CreateView,LoginRequiredMixin):
    model = InventoryProduct
    template_name = 'inventoryProductCreate.html'
    fields = "__all__"
    
class InventoryProductListView(ListView,LoginRequiredMixin):
    model = InventoryProduct
    template_name = 'inventoryProductList.html'
    
class InventoryProductUpdateView(UpdateView,LoginRequiredMixin):
    model = InventoryProduct
    template_name = 'inventoryProductUpdate.html'
    fields = "__all__"
    
class InventoryProductDeleteView(DeleteView,LoginRequiredMixin):
    model = InventoryProduct
    template_name = 'inventoryProductDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('inventoryProductList')
    
  
#admin order create view is meaningless here 
# class AdminOrderCreateView(CreateView,LoginRequiredMixin):
#     model = Order
#     template_name = 'adminOrderCreate.html'
#     fields = ["product",'quantity','status']
    
class AdminOrderListView(ListView,LoginRequiredMixin):
    model = Order
    template_name = 'adminOrderList.html'
    
class AdminOrderUpdateView(UpdateView,LoginRequiredMixin):
    model = Order
    template_name = 'adminOrderUpdate.html'
    fields = ["product",'quantity','status']
    
class AdminOrderDeleteView(DeleteView,LoginRequiredMixin):
    model = Order
    template_name = 'adminOrderDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('adminOrderList')
   
   
   
 
#user level
class HomePage(LoginRequiredMixin,ListView):
    model = ProductVariation
    template_name= 'home.html'


class UserProductList(ListView,LoginRequiredMixin):
    model = InventoryProduct
    template_name = 'userProductList.html'
    
    def get_queryset(self):
        variation_id = self.kwargs['pk']

        product_ids = InventoryProduct.objects.filter(productId__pType_id=variation_id).values_list('productId_id', flat=True)
        
        return InventoryProduct.objects.filter(inventoryId__cityId=self.request.user.city,id__in=product_ids)
    

#user order ruls
@login_required(login_url='login')
def userOrderSubmitView(request, pk):
    if request.method == 'POST':
        product = InventoryProduct.objects.get(id=pk)
        quantity = request.POST.get('quantity')
        if product.quantity >= int(quantity):
            product.quantity -= int(quantity)
            product.save()
            newOrder = Order.objects.create(user=request.user, product=product, quantity=quantity)
            newOrder.save()
            return render(request, 'userOrderSuccess.html')
        else:
            return render(request, 'userOrderFail.html')
        
    else:
        product = InventoryProduct.objects.get(id=pk)
        context = {
                'productInventory': product,
            }
        return render(request, 'userOrder.html', context)


class UserOrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name= 'userOrderList.html'
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class About(TemplateView):
    template_name="about.html"