from django.urls import path
from . import views




urlpatterns = [
    path("Myapp/",views.index, name="index"),
]