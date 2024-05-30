from django.db import models


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
        upload_to="product/image", verbose_name="изображение продукта", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория",
        related_name="products"
    )
    price = models.FloatField(verbose_name="цена продукта")
    created_at = models.DateField(verbose_name="дата создания записи о продукте")
    updated_at = models.DateField(verbose_name="дата изменения записи о продукте")

    def __str__(self):
        return f"{self.name}: {self.description}, цена: {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price", "category"]
