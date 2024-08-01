from django.urls import path
from .views import pdf_to_word_view

urlpatterns = [
    path('', pdf_to_word_view, name='pdf_to_word'),
]
