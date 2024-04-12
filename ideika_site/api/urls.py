from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


"""
TODO: убрать csrf_exempt()
временно все функции обернуты в csrf_exempt(func), чтобы был отключен встроеннный 
механизм защиты от csrf-атак. Он заключается в том, при каждой новой сессии пользователю
выдается токен, без которого не проходят POST, PUT, DELETE запросы.
Чтобы облегчить тестирование, защита выключена

https://stackoverflow.com/questions/50732815/how-to-use-csrf-token-in-django-restful-api-and-react
"""

urlpatterns = [
    path('', views.index),
    path('cards/', csrf_exempt(views.CardsView.as_view())),
    path('cards/<int:card_id>/', csrf_exempt(views.CardsIdView.as_view())),
    path('users/<int:user_id>/cards/', csrf_exempt(views.CardUser.as_view())),
    path('users/<int:user_id>/cards/<int:card_id>/', csrf_exempt(views.CardUser.as_view()))
]
