from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),

]

###################--------------------------PRODUCTS----------------------###########################################################
urlpatterns += [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
urlpatterns += [
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
]


###################--------------------------CUSTOMERS----------------------#######################################################

urlpatterns += [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    
]

urlpatterns += [
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),

]
urlpatterns += [
    path('add_customer/', views.add_customer, name='add_customer'),
]
######################--------------------------ORDERS----------------------#######################################################
urlpatterns += [
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
]

urlpatterns += [
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),

]


urlpatterns += [
    path('add_order/', views.add_order, name='add_order'),
    path('update_orderitem/<int:pk>/', views.update_orderitem, name='update_orderitem'),
    path('delete_orderitem/<int:pk>/', views.delete_orderitem, name='delete_orderitem'),
    path('add_orderitem/', views.add_orderitem, name='add_orderitem'),
]


###################--------------------------login----------------------#######################################################

urlpatterns += [
    path('login/', views.auth_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]








###############################################################################
urlpatterns += [
    path('direct_sale/', views.direct_sale, name='direct_sale'),
    path('update_item/', views.updateItem, name='update_item'),

]












##############################-----------export CSV------------------#######################
urlpatterns += [
    path('customer_csv/', views.customer_csv, name='customer_csv'),
    path('product_csv/', views.product_csv, name='product_csv'),
    path('order_csv/', views.order_csv, name='order_csv'),
    path('orderitem_csv/', views.orderitem_csv, name='orderitem_csv'),

]

################################-----------import CSV------------------#######################
urlpatterns += [
    path('customer_import/', views.import_csv_customer, name='customer_import'),
    path('product_import/', views.import_csv_product, name='product_import'),
    path('order_import/', views.import_csv_order, name='order_import'),
    path('orderitem_import/', views.import_csv_orderitem, name='orderitem_import'),
]


urlpatterns += [
    path('lobby/', views.lobby, name='lobby'),
]