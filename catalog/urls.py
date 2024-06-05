from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product, base

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="index"),
    path("contacts/", contacts, name="contacts"),
    path("product/", product, name="product"),
    path("base/", base, name="base")
]
