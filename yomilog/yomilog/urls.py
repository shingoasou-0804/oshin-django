from app import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/insert", views.insert_log),
    path("api/read", views.read_log),
    path("", views.index),
]
