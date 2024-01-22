from django.urls import path
from . import views
urlpatterns = [
    path("get_analysis", views.get_analysis),
]