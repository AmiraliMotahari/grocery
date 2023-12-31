from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('adminHome/', AdminPage.as_view(), name='adminHome'),
    path('adminHome/cityList/', CityListView.as_view(), name='cityList'),
    path('adminHome/cityCreate/', CityCreateView.as_view(), name='cityCreate'),
    path('adminHome/cityUpdate/<int:pk>/', CityUpdateView.as_view(), name='cityUpdate'),
    path('adminHome/cityDelete/<int:pk>/', CityDeleteView.as_view(), name='cityDelete'),
    path('adminHome/productList/', ProductListView.as_view(), name='productList'),
    path('adminHome/productCreate/', ProductCreateView.as_view(), name='productCreate'),
    path('adminHome/productUpdate/<int:pk>/', ProductUpdateView.as_view(), name='productUpdate'),
    path('adminHome/productDelete/<int:pk>/', ProductDeleteView.as_view(), name='productDelete'),
    path('adminHome/productVariationList/', ProductVariationListView.as_view(), name='productVariationList'),
    path('adminHome/productVariationCreate/', ProductVariationCreateView.as_view(), name='productVariationCreate'),
    path('adminHome/productVariationUpdate/<int:pk>/', ProductVariationUpdateView.as_view(), name='productVariationUpdate'),
    path('adminHome/productVariationDelete/<int:pk>/', ProductVariationDeleteView.as_view(), name='productVariationDelete'),
    path('adminHome/supplierList/', SupplierListView.as_view(), name='supplierList'),
    path('adminHome/supplierCreate/', SupplierCreateView.as_view(), name='supplierCreate'),
    path('adminHome/supplierUpdate/<int:pk>/', SupplierUpdateView.as_view(), name='supplierUpdate'),
    path('adminHome/supplierDelete/<int:pk>/', SupplierDeleteView.as_view(), name='supplierDelete'),
    path('adminHome/inventoryList/', InventoryListView.as_view(), name='inventoryList'),
    path('adminHome/inventoryCreate/', InventoryCreateView.as_view(), name='inventoryCreate'),
    path('adminHome/inventoryUpdate/<int:pk>/', InventoryUpdateView.as_view(), name='inventoryUpdate'),
    path('adminHome/inventoryDelete/<int:pk>/', InventoryDeleteView.as_view(), name='inventoryDelete'),
    path('adminHome/inventoryProductList/', InventoryProductListView.as_view(), name='inventoryProductList'),
    path('adminHome/inventoryProductCreate/', InventoryProductCreateView.as_view(), name='inventoryProductCreate'),
    path('adminHome/inventoryProductUpdate/<int:pk>/', InventoryProductUpdateView.as_view(), name='inventoryProductUpdate'),
    path('adminHome/inventoryProductDelete/<int:pk>/', InventoryProductDeleteView.as_view(), name='inventoryProductDelete'),
    path('adminHome/adminOrderList/', AdminOrderListView.as_view(), name='adminOrderList'),
    # path('adminHome/adminOrderCreate/', AdminOrderCreateView.as_view(), name='adminOrderCreate'),
    path('adminHome/adminOrderUpdate/<int:pk>/', AdminOrderUpdateView.as_view(), name='adminOrderUpdate'),
    path('adminHome/adminOrderDelete/<int:pk>/', AdminOrderDeleteView.as_view(), name='adminOrderDelete'),
    path('userProductList/<int:pk>', UserProductList.as_view(), name='userProductList'),
    path('userOrder/<int:pk>', userOrderSubmitView, name='userOrder'),
    path('userOrderList/', UserOrderList.as_view(), name='userOrderList'),
    path('about/', About.as_view(), name='about'),
    path('viewAllProducts/', ViewAllProducts.as_view(), name='viewAllProducts'),
    path('adminHome/adminImageList/', AdminImageList.as_view(), name='adminImageList'),
    path('adminHome/adminImageCreate/', AdminImageCreate.as_view(), name='adminImageCreate'),
    path('adminHome/adminImageUpdate/<int:pk>', AdminImageUpdate.as_view(), name='adminImageUpdate'),
    path('adminHome/adminImageDelete/<int:pk>', AdminImageDelete.as_view(), name='adminImageDelete'),
    # path('adminHome/swiperList/', SwiperList.as_view(), name='swiperList'),
    # path('adminHome/swiperCreate/', SwiperCreate.as_view(), name='swiperCreate'),
    # path('adminHome/swiperUpdate/<int:pk>', SwiperUpdate.as_view(), name='swiperUpdate'),
    # path('adminHome/swiperDelete/<int:pk>', SwiperDelete.as_view(), name='swiperDelete'),
]
