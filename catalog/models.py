from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="название категории")
    description = models.TextField(verbose_name="описание категории")

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="название продукта")
    description = models.TextField(verbose_name="описание продукта")
    image = models.ImageField(
        upload_to="product/image",
        verbose_name="изображение продукта",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория",
        related_name="products",
    )
    price = models.FloatField(verbose_name="цена продукта")
    created_at = models.DateField(verbose_name="дата создания записи о продукте")
    updated_at = models.DateField(verbose_name="дата изменения записи о продукте")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="owner", related_name="products")

    def __str__(self):
        return f"{self.name}: {self.description}, цена: {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price", "category"]


class Version(models.Model):
    version_number = models.FloatField(verbose_name='version_number')
    product = models.ForeignKey(Product, verbose_name='product', related_name='version', on_delete=models.CASCADE)
    version_name = models.CharField(max_length=100, verbose_name='version_name')
    version_is_active = models.BooleanField(default=False, verbose_name='is_active')

    def __str__(self):
        return f"{self.version_number}: {self.version_name}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
