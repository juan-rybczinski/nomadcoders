import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users.models import User


class Command(BaseCommand):
    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        all_users = User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()
        created_clean = flatten(created_rooms.values())
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                    room=room,
                )
            for amenity in amenities:
                magin_number = random.randint(0, 15)
                if magin_number % 2 == 0:
                    room.amenities.add(amenity)
            for facility in facilities:
                magin_number = random.randint(0, 15)
                if magin_number % 2 == 0:
                    room.facilities.add(facility)
            for rule in rules:
                magin_number = random.randint(0, 15)
                if magin_number % 2 == 0:
                    room.house_rules.add(rule)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
