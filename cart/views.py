from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product
from django.views.generic import FormView, View

from coupons.forms import CouponApplyForm
from .forms import CartAddProductForm
from .cart import Cart


class CartAdd(FormView):
    http_method_names = ['post']
    form_class = CartAddProductForm

    def post(self, request, product_id, *args, **kwargs):
        self.cart = Cart(request)
        self.product = get_object_or_404(Product, id=product_id)
        return super(CartAdd, self).post(request, product_id, *args, **kwargs)

    def form_valid(self, form):
        cd = form.cleaned_data
        self.cart.add(product=self.product,
                      quantity=cd['quantity'],
                      update_quantity=cd['update'])
        return redirect('cart:cart_detail')


class CartRemove(View):

    def get(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetail(View):
    template_name = 'cart/detail.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        coupon_apply_form = CouponApplyForm()

        for item in cart:
            print(str(item['update_quantity_form']))

        # r = Recommender()
        # cart_products = [item['product'] for item in cart]
        # recommended_products = r.suggest_products_for(cart_products, max_results=4)

        return render(request,
                      self.template_name,
                      {'cart': cart,
                       'coupon_apply_form': coupon_apply_form})
        #    'recommended_products': recommended_products})
