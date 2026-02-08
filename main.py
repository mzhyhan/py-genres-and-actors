import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    Actor.objects.all().delete()
    Genre.objects.all().delete()

    Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Dramma")

    george = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    drama.name = "Drama"
    drama.save()
    george.last_name = "Clooney"
    george.save()
    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    action.delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
