from django.urls import path, register_converter
from . import views
from . import converters
from django.views.decorators.csrf import csrf_exempt


"""
https://docs.djangoproject.com/en/5.0/topics/http/urls/#passing-extra-options-to-view-functions
как дополнительно передавать аргументы в view
"""

urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('cards/', views.CardsView.as_view()),  # все карточки
    path('cards/<int:card_id>/', views.OneCardView.as_view()),  # отдельная карточка
    path('users/<int:user_id>/', views.UserView.as_view()),
    path('users/<int:user_id>/cards/', views.CategoryView.as_view()),  # коллекция
    path('users/<int:user_id>/cards/<int:card_id>/', views.CategoryView.as_view()),  # одна карточка из коллекции
    path('cards/<int:card_id>/tags/', views.CategoryView.as_view()),  # теги карточки
    path('cards/<int:card_id>/tags/<int:tag_id>', views.CategoryView.as_view()),  # теги карточки
]
