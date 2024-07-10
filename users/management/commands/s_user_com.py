from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='Admin@one.click',
            first_name='Admin',
            last_name='One_click',
            is_staff=True,
            is_superuser=True,

        )
        user.set_password('admin123')
        user.save()
