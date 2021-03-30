from django.views.generic import ListView
from django.shortcuts import render
from . import models


class RoomList(ListView):

    """ RoomList Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    return render(request, "rooms/room_detail.html")
