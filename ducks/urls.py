from django.urls import path, include
from django.conf import settings
from .views import record_list, record_edit, record_add, record_del
from .views import dashboard, graph1

urlpatterns = [
    path("list/", record_list, name="record_list"),
    path("edit/<int:pk>", record_edit, name="record_edit"),
    path("delete/<int:pk>", record_del, name="record_del"),
    path("add/", record_add, name="record_add"),
    path("graph/1", graph1, name="graph1"),
    path("dashboard", dashboard, name="dashboard"),
]
