from django.urls import path

from .views import *

urlpatterns = [
    path('load_file_tables/', countTableUsability.as_view()),
    path('load_file_user/', countUserActivity.as_view())
]
