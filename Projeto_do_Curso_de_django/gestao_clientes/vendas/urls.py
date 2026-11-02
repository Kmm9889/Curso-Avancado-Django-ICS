from django.urls import path
from .views import (
    DashboardView, NovoPedido, NovoItemPedido, ListaVendas, EditPedido
)

urlpatterns = [
    path('', ListaVendas.as_view(), name='lista-vendas'),
    path('novo-pedido/', NovoPedido.as_view(), name='novo-pedido'),
    path('novo-item-pedido/<int:venda>/', NovoItemPedido.as_view(), name='novo-item-pedido'),
    path('editar-pedido/<int:venda_id>/', EditPedido.as_view(), name='editar-pedido'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]