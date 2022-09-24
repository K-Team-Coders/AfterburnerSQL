from django.urls import path

from .views import *

urlpatterns = [
    path('load_file_tables/', countTableUsability.as_view()),
    path('load_file_users/', countUserActivity.as_view()),
    path('predict_query_time_execution/<str:query>/', predictQueryResponseTime.as_view()),
    path('predict_query_time_execution_operators/<str:query>/', predictQueryResponseTimeOperatorsCount.as_view()),
    path('predictQueryResponseTimeDesicionTree/<str:query>/', predictQueryResponseTimeDesicionTree.as_view())
]
