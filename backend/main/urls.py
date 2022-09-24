from django.urls import path

from .views import *

urlpatterns = [
    path('load_file/', loadFile.as_view())
]
