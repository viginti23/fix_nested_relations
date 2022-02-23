from django.urls import path, include

from product import views

urlpatterns = [
    path('popular-products/', views.PopularProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),

    path('variants/<slug:product_slug>/', views.ProductVariantDetail.as_view()),
    path('toppings/<slug:category_slug>/', views.ProductToppingDetail.as_view()),

]