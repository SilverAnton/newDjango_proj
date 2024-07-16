from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_category_from_cache():
    category_all = Category.objects.all()
    if not CACHE_ENABLED:
        return category_all
    key = 'category_list'
    category = cache.get(key)
    if category is None:
        cache.set(key, category_all)
        return category_all
    return category








