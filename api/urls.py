from django.urls import path
from .views import *
from api import views


urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/',views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),    


]
