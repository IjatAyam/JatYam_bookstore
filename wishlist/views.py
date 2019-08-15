from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, FormView
from django.http import JsonResponse

from common.decorators import ajax_required
from shop.models import Product
from .wishlist import Wishlist


class WishlistDetail(View):
    template_name = 'wishlist/detail.html'

    def get(self, request, *args, **kwargs):
        wishlist = Wishlist(request)

        return render(request,
                      self.template_name,
                      {'wishlist': wishlist})


class WishlistAdd(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        wishlist = Wishlist(request)
        product_id = request.POST.get('id')
        if request.is_ajax():
            if product_id:
                try:
                    product = Product.objects.get(id=product_id)
                    wishlist.add(product=product)
                    return JsonResponse({'status': 'ok'})
                except:
                    pass
        return JsonResponse({'status': 'ko'})


class WishlistRemove(View):

    def get(self, request, product_id, *args, **kwargs):
        wishlist = Wishlist(request)
        product = get_object_or_404(Product, id=product_id)
        wishlist.remove(product)
        return redirect('wishlist:wishlist_detail')
