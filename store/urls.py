from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),

	path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order")
]