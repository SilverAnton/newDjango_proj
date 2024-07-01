from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (HomePageView, BasePageView, ContactsPageView, ProductListView,
                           ProductDetailView, CategoryListView, CategoryDetailView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)


app_name = CatalogConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("product_create/catalog", ProductCreateView.as_view(), name="product_create"),
    path("product_list/catalog", ProductListView.as_view(), name="product_list"),
    path("product_detail/catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_edit/catalog/<int:pk>/", ProductUpdateView.as_view(), name="product_edit"),
    path("product_delete/catalog/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("category/catalog/", CategoryListView.as_view(), name="category"),
    path("base/", BasePageView.as_view(), name="base"),
    path("category_review/catalog/<int:pk>/", CategoryDetailView.as_view(), name="category_review"),



]
