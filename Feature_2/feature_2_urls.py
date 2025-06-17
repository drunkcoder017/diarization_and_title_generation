from django.urls import path
from feature_2_urls import generate_titles_api

urlpatterns = [
    path('api/generate-titles/', generate_titles_api, name='generate_titles_api'),
]
