from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('', views.home, name='home'),
     path('about/', views.about_view, name='about'),
     path('contact/', views.contact_view, name='contact'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.place_order, name='checkout'),
       path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
     path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
      path('signup/',views.signup_view,name='signup'),]