from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.utils.text import slugify

from catalog.forms import ProductForm
from catalog.models import Product, Category
from version.forms import VersionForm
from version.models import Version


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.object.pk])


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


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))
    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.object.pk])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class CategoryDetailView(DetailView):
    model = Category
