# from django.urls import path
# from .import views

# urlpatterns=[
#     path('',views.product_list,name='product_list'),
#     path('<int:id>/',views.product_detail,name='product_detail'),
#     path('api/products/', views.product_api, name='product_api'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),

    # CRUD
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),

    # API
    path('api/products/', views.product_api, name='product_api'),
]