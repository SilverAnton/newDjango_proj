
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.utils.text import slugify
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
    fields = ['title', 'content', 'is_published']
    success_url = reverse_lazy("catalog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:blog_detail", args=[self.object.pk])

    #def form_valid(self, form):
        #if form.is_valid():
            #new_blog = form.save
            #new_blog.slug = slugify(new_blog.title)
            #new_blog.save()
        #return super().form_valid(form)

    #def get_success_url(self):
        #return reverse_lazy("catalog:blogpost_detail", args=[self.object.pk])

class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'slug', 'content']
    success_url = reverse_lazy("catalog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:blog_detail", args=[self.object.pk])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_list")
