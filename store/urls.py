from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('cart/', views.cart, name='cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('update_cart/', views.update_cart, name='update_cart'),

    path('process_order/', views.process_order, name='process_order'),

    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
