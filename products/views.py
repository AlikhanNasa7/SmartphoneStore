from django.shortcuts import render, redirect
from .models import Product, Category, Basket
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Store'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_slug = self.kwargs.get('category_slug')
        return queryset.filter(category__slug=category_slug) if category_slug else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Store - Каталог'
        context['categories'] = Category.objects.all()
        return context


def products(request, category_slug=None, page=1):
    store_products = Product.objects.filter(category__slug=category_slug) if category_slug else Product.objects.all()

    paginator = Paginator(store_products, 3)
    products_paginator = paginator.page(page)

    context = {
        'title': 'Store - Каталог',
        'products': products_paginator,
        'categories': Category.objects.all(),
        'paginator': paginator,
        'is_paginated': True,
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    needed_product = Product.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=needed_product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=needed_product, quantity=1)
    else:
        basket_item = baskets.first()
        basket_item.quantity += 1
        basket_item.save()
    return redirect('users:profile', pk=request.user.pk)


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect('users:profile', pk=request.user.pk)
