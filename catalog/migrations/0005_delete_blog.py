# Generated by Django 5.0.6 on 2024-06-26 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_blog_options"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Blog",
        ),
    ]
