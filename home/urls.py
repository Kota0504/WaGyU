from django.urls import path 
from .views import PartsList, parts_detail


urlpatterns = [
        path('list/', PartsList.as_view(), name='list'),
        path('detail/<int:pk>/', parts_detail, name='detail'),
]
