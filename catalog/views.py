import reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Category, Blog


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactsPageView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductListView(ListView):
    model = Product


class CategoryListView(ListView):
    model = Category


class BasePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(DetailView):
    model = Product


class CategoryDetailView(DetailView):
    model = Category


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'slug', 'content']
    success_url = reverse_lazy("catalog:blog_list")



class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'slug', 'content']
    success_url = reverse_lazy("catalog:blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_list")