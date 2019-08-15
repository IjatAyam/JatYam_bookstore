from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.WishlistDetail.as_view(), name='wishlist_detail'),
    path('add/',
         views.WishlistAdd.as_view(),
         name='wishlist_add'),
    path('remove/<int:product_id>/',
         views.WishlistRemove.as_view(),
         name='wishlist_remove'),
]
