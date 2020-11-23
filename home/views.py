from django.shortcuts import render
from django.views.generic import ListView
from .models import PartsModel


class PartsList(ListView):
    template_name = 'parts_list.html'
    model = PartsModel


def parts_detail(request, pk):
    obj = PartsModel.objects.get(pk=pk)
    template = obj.template
    print(template)
    return render(request, template)

