from django.urls import path
from .views import *
urlpatterns = [
    path("get/",get,name='get'),
    path('products/<pk>',products,name='products'),
    path("delete/<pk>",delete,name='delete')
]