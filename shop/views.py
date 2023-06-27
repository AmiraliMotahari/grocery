from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView, DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
    
    
    
    
    
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
    template_name = 'ProductVariationList.html'
    
class ProductVariationUpdateView(UpdateView):
    model = ProductVariation
    template_name = 'productVariationUpdate.html'
    fields = ['name']
    
class ProductVariationDeleteView(DeleteView):
    model = ProductVariation
    template_name = 'productVariationDelete.html'
    fields = ['name']
    success_url = reverse_lazy('productVariationList')
    
    
class supplierCreateView(CreateView):
    model = Supplier
    template_name = 'supplierCreate.html'
    fields = "__all__"
    
class supplierListView(ListView):
    model = Supplier
    template_name = 'supplierList.html'
    
class supplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'supplierUpdate.html'
    fields = "__all__"
    
class supplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplierDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('supplierList')
    
    
class inventoryCreateView(CreateView):
    model = Inventory
    template_name = 'inventoryCreate.html'
    fields = "__all__"
    
class inventoryListView(ListView):
    model = Inventory
    template_name = 'inventoryList.html'
    
class inventoryUpdateView(UpdateView):
    model = Inventory
    template_name = 'inventoryUpdate.html'
    fields = "__all__"
    
class inventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventoryDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('inventoryList')
    
class inventoryProductCreateView(CreateView):
    model = InventoryProduct
    template_name = 'inventoryProductCreate.html'
    fields = "__all__"
    
class inventoryProductListView(ListView):
    model = InventoryProduct
    template_name = 'inventoryProductList.html'
    
class inventoryProductUpdateView(UpdateView):
    model = InventoryProduct
    template_name = 'inventoryProductUpdate.html'
    fields = "__all__"
    
class inventoryProductDeleteView(DeleteView):
    model = InventoryProduct
    template_name = 'inventoryProductDelete.html'
    fields = "__all__"
    success_url = reverse_lazy('inventoryProductList')