from django.urls import path
from .views import add_note, note_list

urlpatterns = [
    path('add/', add_note, name='add_note'),
    path('', note_list, name='note_list'),
]
