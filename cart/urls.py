from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartDetail.as_view(), name='cart_detail'),
    path('add/',
         views.CartAdd.as_view(),
         name='cart_add'),
    path('remove/',
         views.CartRemove.as_view(),
         name='cart_remove'),
]
