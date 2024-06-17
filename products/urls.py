from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/<slug:category_slug>/', views.ProductListView.as_view(), name='category'),
    #path('products/<slug:category_slug>/', views.ProductListView.as_view(), name='category-paginator'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('page/<int:page>', views.ProductListView.as_view(), name='paginator'),
    path('basket/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]