from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PartsModel

class PartsList(ListView):
    template_name = 'parts_list.html'
    model = PartsModel

class PartsDetail(DetailView):
    template_name = 'parts_detail.html'
    model = PartsModel
