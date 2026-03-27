from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('frequent_questions', views.frequent_questions)
]
 