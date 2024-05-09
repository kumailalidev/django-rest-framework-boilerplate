from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("ping/", views.ping, name="ping"),
    path("upload/", views.image_upload, name="upload"),
]
