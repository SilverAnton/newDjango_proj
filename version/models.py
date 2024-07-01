from django.db import models

from catalog.models import Product


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='version', on_delete=models.CASCADE)
    version_number = models.FloatField(verbose_name='version_number')
    version_name = models.CharField(max_length=100, verbose_name='version_name')
    version_is_active = models.BooleanField(default=False, verbose_name='is_active')

    def __str__(self):
        return f"{self.version_number}: {self.version_name}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
