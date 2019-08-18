from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator

from common.decorators import ajax_required
from shop.models import Product
from coupons.forms import CouponApplyForm
from .forms import CartAddProductForm
from .cart import Cart


class CartAdd(View):
    http_method_names = ['post']

    @method_decorator(ajax_required)
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')
        update = request.POST.get('update')
        if product_id and quantity and update:
            try:
                product = Product.objects.get(id=product_id)
                cart.add(product=product,
                         quantity=int(quantity),
                         update_quantity=bool(update == "True"))
                return JsonResponse({'status': 'ok'})
            except:
                pass
        return JsonResponse({'status': 'ko'})


class CartRemove(View):
    http_method_names = ['post']

    @method_decorator(ajax_required)
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get('id')
        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                cart.remove(product)
                return JsonResponse({'status': 'ok'})
            except:
                pass
        return JsonResponse({'status': 'ko'})


class CartDetail(View):
    template_name = 'cart/detail.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        coupon_apply_form = CouponApplyForm()

        # r = Recommender()
        # cart_products = [item['product'] for item in cart]
        # recommended_products = r.suggest_products_for(cart_products, max_results=4)

        return render(request,
                      self.template_name,
                      {'cart': cart,
                       'coupon_apply_form': coupon_apply_form})
        #    'recommended_products': recommended_products})
