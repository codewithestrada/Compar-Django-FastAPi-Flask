from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_events, name='get_events'),
    path('evento/<int:evento_id>/', views.get_by_id, name='id'),
    path('crear/', views.create_event, name='create'),
]
