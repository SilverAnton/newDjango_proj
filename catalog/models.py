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

    def __str__(self):
        return f"{self.name}: {self.description}, цена: {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price", "category"]


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="заголовок")
    slug = models.CharField(max_length=100, verbose_name="slug")
    content = models.TextField(verbose_name='содержимое')
    image_preview = models.ImageField(
        upload_to="blog/image",
        verbose_name="предварительный просмотр",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=False, verbose_name="опубликованные посты")
    views_count = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")

    def __str__(self):
        return f"{self.title}: {self.content}"

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ["title", "slug"]