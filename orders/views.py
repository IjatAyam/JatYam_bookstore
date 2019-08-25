from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from coupons.forms import CouponApplyCheckout


class OrderCreate(CreateView):
    template_name = 'orders/order/create.html'
    form_class = OrderCreateForm
    model = Order
    success_url = reverse_lazy('shop:product_list')

    def dispatch(self, request, *args, **kwargs):
        self.cart = Cart(request)
        self.session = request.session
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        order = form.save(commit=False)
        if self.cart.coupon:
            order.coupon = self.cart.coupon
            order.discount = self.cart.coupon.discount
        order.save()
        for item in self.cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        self.cart.clear()
        self.session['order_id'] = order.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coupon_apply_form"] = CouponApplyCheckout()
        return context
