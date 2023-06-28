from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView, DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# class HomePage(TemplateView):
#     template_name = 'home.html'
    
    
    
    
    
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
    
class CityListView(ListView):
    model = City
    template_name = 'cityList.html'
    
class CityUpdateView(UpdateView):
    model = City
    template_name = 'cityUpdate.html'
    fields = ['name']
    
class CityDeleteView(DeleteView):
    model = City
    template_name = 'cityDelete.html'
    fields = ['name']
    success_url = reverse_lazy('cityList')
    
    
    
    
    
class ProductCreateView(CreateView):
    model = Product
    template_name = 'productCreate.html'
    fields = ['name','price', 'quantity', 'pType', 'cityId']
    
class ProductListView(ListView):
    model = Product
    template_name = 'productList.html'
    
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'productUpdate.html'
    fields = ['name','price', 'quantity', 'pType', 'cityId']
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'productDelete.html'
    fields = ['name','price', 'quantity', 'pType', 'cityId']
    success_url = reverse_lazy('productList')



class ProductVariationCreateView(CreateView):
    model = ProductVariation
    template_name = 'productVariationCreate.html'
    fields = ['name']
    
class ProductVariationListView(ListView):
    model = ProductVariation
    template_name = 'productVariationList.html'
    
class ProductVariationUpdateView(UpdateView):
    model = ProductVariation
    template_name = 'productVariationUpdate.html'
    fields = ['name']
    
class ProductVariationDeleteView(DeleteView):
    model = ProductVariation
    template_name = 'productVariationDelete.html'
    fields = ['name']
    success_url = reverse_lazy('productVariationList')

    
class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'supplierCreate.html'
    fields = "__all__"
    
class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplierList.html'
    
class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'supplierUpdate.html'
    fields = "__all__"
    
class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplierDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('supplierList')
    
    
class InventoryCreateView(CreateView):
    model = Inventory
    template_name = 'inventoryCreate.html'
    fields = "__all__"
    
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventoryList.html'
    
class InventoryUpdateView(UpdateView):
    model = Inventory
    template_name = 'inventoryUpdate.html'
    fields = "__all__"
    
class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventoryDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('inventoryList')
    
    
    
class InventoryProductCreateView(CreateView):
    model = InventoryProduct
    template_name = 'inventoryProductCreate.html'
    fields = "__all__"
    
class InventoryProductListView(ListView):
    model = InventoryProduct
    template_name = 'inventoryProductList.html'
    
class InventoryProductUpdateView(UpdateView):
    model = InventoryProduct
    template_name = 'inventoryProductUpdate.html'
    fields = "__all__"
    
class InventoryProductDeleteView(DeleteView):
    model = InventoryProduct
    template_name = 'inventoryProductDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('inventoryProductList')
    
  
    
class AdminOrderCreateView(CreateView):
    model = Order
    template_name = 'adminOrderCreate.html'
    fields = "__all__"
    
class AdminOrderListView(ListView):
    model = Order
    template_name = 'adminOrderList.html'
    
class AdminOrderUpdateView(UpdateView):
    model = Order
    template_name = 'adminOrderUpdate.html'
    fields = "__all__"
    
class AdminOrderDeleteView(DeleteView):
    model = Order
    template_name = 'adminOrderDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('adminOrderList')
   
   
   
 
#user level
class HomePage(LoginRequiredMixin,ListView):
    model = ProductVariation
    template_name= 'home.html'


class UserProductList(ListView):
    model = InventoryProduct
    template_name = 'userProductList.html'
    
    def get_queryset(self):
        variation_id = self.kwargs['pk']
        # return InventoryProduct.objects.filter(productId__id=variation_id)

        product_ids = InventoryProduct.objects.filter(productId__pType_id=variation_id).values_list('productId_id', flat=True)
        
        return InventoryProduct.objects.filter(id__in=product_ids)

# class UserProductBuy(LoginRequiredMixin,ListView):
#     model = InventoryProduct
#     template_name= 'userOrder.html'
    
#     def get_queryset(self):
#         return InventoryProduct.objects.filter(inventory__city=self.request.user.city)

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