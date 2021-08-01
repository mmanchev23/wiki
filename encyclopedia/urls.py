from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("wiki/<str:title>", views.entry_view, name="entry"),
    path("create", views.create_view, name="create"),
    path("edit/<str:title>", views.edit_view, name="edit"),
    path("wiki/", views.random_page_view, name="random")
]
