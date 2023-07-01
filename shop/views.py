from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView, DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
# from .forms import POSTForm
   
    
#admin pages
class AdminPage(LoginRequiredMixin, TemplateView,):
    template_name = 'adminHome.html'  
    
class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    template_name = 'cityCreate.html'
    fields = ['name']
    
# class CityDetailView(LoginRequiredMixin, DetailView):
#     model = City
#     template_name = 'forms_create.html'
    
class CityListView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'cityList.html'
    
class CityUpdateView(LoginRequiredMixin, UpdateView):
    model = City
    template_name = 'cityUpdate.html'
    fields = ['name']
    
class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'cityDelete.html'
    fields = ['name']
    success_url = reverse_lazy(LoginRequiredMixin, 'cityList')
    
    
    
    
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'productCreate.html'
    fields = '__all__'
    
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'productList.html'
    
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'productUpdate.html'
    fields = '__all__'
    
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'productDelete.html'
    fields = '__all__'
    success_url = reverse_lazy(LoginRequiredMixin, 'productList')



class ProductVariationCreateView(LoginRequiredMixin, CreateView):
    model = ProductVariation
    template_name = 'productVariationCreate.html'
    fields = '__all__'
    
class ProductVariationListView(LoginRequiredMixin, ListView):
    model = ProductVariation
    template_name = 'productVariationList.html'
    
class ProductVariationUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductVariation
    template_name = 'productVariationUpdate.html'
    fields = '__all__'
    
class ProductVariationDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductVariation
    template_name = 'productVariationDelete.html'
    fields = '__all__'
    success_url = reverse_lazy(LoginRequiredMixin, 'productVariationList')

    
class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    template_name = 'supplierCreate.html'
    fields = "__all__"
    
class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplierList.html'
    
class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    template_name = 'supplierUpdate.html'
    fields = "__all__"
    
class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplierDelete.html'
    fields = "__all__"
    success_url = reverse_lazy(LoginRequiredMixin, 'supplierList')
    
    
class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    template_name = 'inventoryCreate.html'
    fields = "__all__"
    
class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventoryList.html'
    
class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Inventory
    template_name = 'inventoryUpdate.html'
    fields = "__all__"
    
class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Inventory
    template_name = 'inventoryDelete.html'
    fields = "__all__"
    success_url = reverse_lazy(LoginRequiredMixin, 'inventoryList')
    
    
    
class InventoryProductCreateView(LoginRequiredMixin, CreateView):
    model = InventoryProduct
    template_name = 'inventoryProductCreate.html'
    fields = "__all__"
    
class InventoryProductListView(LoginRequiredMixin, ListView):
    model = InventoryProduct
    template_name = 'inventoryProductList.html'
    
class InventoryProductUpdateView(LoginRequiredMixin, UpdateView):
    model = InventoryProduct
    template_name = 'inventoryProductUpdate.html'
    fields = "__all__"
    
class InventoryProductDeleteView(LoginRequiredMixin, DeleteView):
    model = InventoryProduct
    template_name = 'inventoryProductDelete.html'
    fields = "__all__"
    success_url = reverse_lazy(LoginRequiredMixin, 'inventoryProductList')
    
  
#admin order create view is meaningless here 
# class AdminOrderCreateView(LoginRequiredMixin, CreateView):
#     model = Order
#     template_name = 'adminOrderCreate.html'
#     fields = ["product",'quantity','status']
    
class AdminOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'adminOrderList.html'
    
class AdminOrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'adminOrderUpdate.html'
    fields = ["product",'quantity','status']
    
class AdminOrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'adminOrderDelete.html'
    fields = "__all__"
    success_url = reverse_lazy(LoginRequiredMixin, 'adminOrderList')
    
   
class AdminImageCreate(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'adminImageCreate.html'
    fields = "__all__"
    
class AdminImageList(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'adminImageList.html'
    
class AdminImageUpdate(LoginRequiredMixin, UpdateView):
    model = Image
    template_name = 'adminImageUpdate.html'
    fields = "__all__"
    
class AdminImageDelete(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'adminImageDelete.html'
    fields = "__all__"
    success_url = reverse_lazy(LoginRequiredMixin, 'adminImageList')
   
   
# class SwiperCreate(LoginRequiredMixin, CreateView):
#     model = Swiper
#     template_name = 'swiperCreate.html'
#     fields = "__all__"
    
# class SwiperList(LoginRequiredMixin, ListView):
#     model = Swiper
#     template_name = 'swiperList.html'
    
# class SwiperUpdate(LoginRequiredMixin, UpdateView):
#     model = Swiper
#     template_name = 'swiperUpdate.html'
#     fields = "__all__"
    
# class SwiperDelete(LoginRequiredMixin, DeleteView):
#     model = Swiper
#     template_name = 'swiperDelete.html'
#     fields = "__all__"
#     success_url = reverse_lazy('swiperList')
   
   
   
 
#user level
class HomePage(ListView):
    model = ProductVariation
    template_name= 'home.html'
    context_object_name = 'pvarlist'
        

class UserProductList(LoginRequiredMixin,ListView):
    model = InventoryProduct
    template_name = 'userProductList.html'
    
    def get_queryset(self):
        variation_id = self.kwargs['pk']

        product_ids = InventoryProduct.objects.filter(productId__pType_id=variation_id).values_list('productId_id', flat=True)
        
        return InventoryProduct.objects.filter(inventoryId__cityId=self.request.user.city, id__in=product_ids)
    

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
    
    
class ViewAllProducts(LoginRequiredMixin,ListView):
    model = InventoryProduct
    template_name = "viewAll.html"
    
    def get_queryset(self):
        return InventoryProduct.objects.filter(inventoryId__cityId=self.request.user.city)