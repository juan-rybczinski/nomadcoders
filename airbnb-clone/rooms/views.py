from django.views.generic import ListView
from django.shortcuts import render
from django.http import Http404
from . import models


class RoomList(ListView):

    """ RoomList Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(
            request,
            "rooms/room_detail.html",
            {
                "room": room,
            },
        )

    except models.Room.DoesNotExist:
        raise Http404()
