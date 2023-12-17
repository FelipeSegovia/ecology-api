from django.urls import path
from ecology.api import ecology_api_view

urlpatterns = [
    path('', ecology_api_view, name='ecology_api')
]