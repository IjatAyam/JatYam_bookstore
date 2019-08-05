from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView


from .models import Product, Category


class ProductListView(ListView):
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        products = super().get_queryset().filter(available=True)
        if 'category_slug' in self.kwargs:
            category = get_object_or_404(
                Category, slug=self.kwargs['category_slug'])
            products = products.filter(category=category)
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
        context['categories'] = Category.objects.all()
        return context
