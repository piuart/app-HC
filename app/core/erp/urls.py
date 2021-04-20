from django.urls import path

from core.chat import views
from core.erp.views.category.views import *
from core.erp.views.client.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.dashboardalmacen.views import DashboardAlmacenView
from core.erp.views.product.views import *
from core.erp.views.sale.view import *
from core.erp.views.tests.views import TestView
from core.erp.views.dashboardventas.views import *
from core.erp.views.listareproduccion.views import *


#from core.youtube.views import YoutubeView
from core.youtube import views

app_name = 'erp'

urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # client
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('dashboardalmacen/', DashboardAlmacenView.as_view(), name='dashboardalmacen'),

    #youtube
    #path('youtube/', YoutubeView.as_view(), name='youtube'),
    

    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # ver ventas
    path('dashboardventas/', DashboardVentasView.as_view(), name='dashboardventas'),
    # sale
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
    path('sale/update/<int:pk>/', SaleUpdateView.as_view(), name='sale_update'),
    path('sale/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),

    # category
    path('listareproduccion/list/', ListaReproduccionListView.as_view(), name='listareproduccion_list'),
    path('listareproduccion/add/', ListaReproduccionCreateView.as_view(), name='listareproduccion_create'),
    path('listareproduccion/update/<int:pk>/', ListaReproduccionUpdateView.as_view(), name='listareproduccion_update'),
    path('listareproduccion/delete/<int:pk>/', ListaReproduccionDeleteView.as_view(), name='listareproduccion_delete'),

    # test-PRUEBAS
    path('test/', TestView.as_view(), name='test'),
]
