from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductsListViews.as_view(), name="products"),
    path('category/<int:category_id>/', views.ProductsListViews.as_view(), name="category"),
    path('page/<int:page>/', views.ProductsListViews.as_view(), name="paginator"),
    path('basket/add/<int:product_id>/', views.basket_add, name="basket_add"),
    path('basket/delete/<int:basket_id>/', views.basket_delete, name="basket_delete"),
]
