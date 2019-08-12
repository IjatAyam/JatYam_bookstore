from django.views.generic import View
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm


class CouponApply(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        now = timezone.now()
        form = CouponApplyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
                request.session['coupon_id'] = coupon.id
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
        return redirect('cart:cart_detail')
