from django.contrib import admin
from django.urls import path
from . import views
#cite views from same folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("cart",views.cart,name="cart"),
    path("add_to_cart", views.add_to_cart, name= "add"),
    path("confirm_payment/<str:pk>", views.confirm_payment, name="add"),
    path("login",views.sign_in,name="login"),
]