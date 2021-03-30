from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class RoomList(ListView):

    """ RoomList Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    model = models.Room


def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(
        request,
        "rooms/room_search.html",
        {
            "city": city,
        },
    )
