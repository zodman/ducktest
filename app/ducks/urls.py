from django.urls import  path, include
from django.conf import settings
from .views import record_list, record_edit, record_add

urlpatterns = [
    path("list", record_list, name="record_list"),
    path("edit/<int:pk>", record_edit, name="record_edit"),
    path("add/", record_add, name="record_add"),
]
