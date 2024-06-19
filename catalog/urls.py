from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomePageView, BasePageView, ContactsPageView, ProductListView, ProductDetailView, CategoryListView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("category/catalog", ProductListView.as_view(), name="product"),
    path("category/catalog/", CategoryListView.as_view(), name="category"),
    path("base/", BasePageView.as_view(), name="base"),
    path("product_review/catalog/<int:pk>/", ProductDetailView.as_view(), name="product_review"),
    path("category_review/catalog/<int:pk>/", CategoryDetailView.as_view(), name="category_review"),

]
