from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.ver_post, name="ver_post"),
]
