from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django import forms

from cart.forms import CartAddProductForm
from .models import Product, Category
from .forms import SearchForm


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    query = None

    def get(self, request, *args, **kwargs):
        if 'query' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                self.query = form.cleaned_data['query']
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        products = super().get_queryset().filter(available=True)
        if 'category_slug' in self.kwargs:
            category = get_object_or_404(
                Category, slug=self.kwargs['category_slug'])
            products = products.filter(category=category)
        if self.query:
            products = products.filter(name__icontains=self.query)
        return products

    def get_context_data(self, **kwargs):
        # Call base context
        context = super().get_context_data(**kwargs)
        # Add catogories
        context['category'] = None
        context['categories'] = Category.objects.all()
        if 'category_slug' in self.kwargs:
            context['category'] = Category.objects.get(
                slug=self.kwargs['category_slug'])
        context['query'] = self.query
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    def get_queryset(self):
        product = super().get_queryset()
        try:
            product.get(slug=self.kwargs['slug'])
        except:
            raise Http404('No product found matching the query')
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        context['categories'] = Category.objects.all()
        return context
