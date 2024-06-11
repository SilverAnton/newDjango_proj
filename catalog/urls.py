from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product, base, product_review, category, category_review

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="index"),
    path("contacts/", contacts, name="contacts"),
    path("product/", product, name="product"),
    path("category/", category, name="category"),
    path("base/", base, name="base"),
    path("product/<int:pk>/", product_review, name="product_review"),
    path("category_review/", category_review, name="category_review"),

]
