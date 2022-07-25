from django.urls import path
from ordersapp import views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='orders_list'),
    path('create/', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', ordersapp.OrderItemsDelete.as_view(), name='order_delete'),
    path('detail/<int:pk>/', ordersapp.OrderItemDetail.as_view(), name='order_read'),
    path('forming/complite/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete')
]
