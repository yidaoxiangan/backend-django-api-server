from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_function, name='create'),
    path('download/', views.download_function, name='download'),
    path('query/', views.query_function, name='query_function'),
    path('upload/', views.upload_function, name='upload'),
]
