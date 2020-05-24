# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableView
import django_tables2 as tables
from django.urls import reverse_lazy
from .models import Record


class RecordTable(tables.Table):
    actions = tables.TemplateColumn(template_name="ducks/_column_actions.html",
                                    orderable=False)
    class Meta:
        model = Record

class RecordList(SuccessMessageMixin, SingleTableView):
    model = Record
    table_class= RecordTable
    paginate_by = 5

record_list = login_required(RecordList.as_view())

class RecordEdit(SuccessMessageMixin,UpdateView):
    model = Record
    fields = "__all__"
    success_url = reverse_lazy("record_list")
    success_message  = "Record updated"

record_edit = login_required(RecordEdit.as_view())


class RecordCreate(SuccessMessageMixin, CreateView):
    model = Record
    fields = "__all__"
    success_url = reverse_lazy("record_list")
    success_message  = "Record created"

record_add = login_required(RecordCreate.as_view())


