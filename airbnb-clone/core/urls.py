from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [path("", room_views.RoomList.as_view(), name="home")]
