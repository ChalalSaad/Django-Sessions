from . import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('load/',views.load_product,name='load'),
    path('shop/',views.shop,name='shop'),
    path('product/<int:product_id>/',views.detail_product,name='detail-product'),


]