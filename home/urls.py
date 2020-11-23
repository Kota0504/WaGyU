from django.urls import path 
from .views import PartsList, PartsDetail


urlpatterns = [
        path('list/', PartsList.as_view(), name='list'),
        path('detail/<int:pk>/', PartsDetail.as_view(), name='detail'),
]
