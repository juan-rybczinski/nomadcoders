from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "This command creates superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="ebadmin")
        if not admin:
            User.objects.create_superuser("ebadmin", "jhreplay.lee@gmail.com", "123456")
            self.stdout.write(self.style.SUCCESS("Superuser created!"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser exists!"))
