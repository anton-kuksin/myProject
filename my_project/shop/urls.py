from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('каталог товаров/', views.catalog, name='catalog'),
    path('товар/<int:product_id>/', views.product_detail, name='product_detail'),
]
