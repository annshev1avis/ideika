from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from api.models import Card, User, CardInUserCollection, Category, Tag
import json
from rest_framework import generics
from rest_framework import mixins

from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers

# Категории
class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer



# Карточки
class CardsListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.filter(is_banned=False)
    serializer_class = serializers.CardSerializer

class CardsByCategoryListView(generics.ListAPIView):
    serializer_class = serializers.CardSerializer

    def get_queryset(self):
        cat_id = self.kwargs['category_id']
        return Card.objects.filter(is_banned=False, category_id=cat_id)


class SingleCardView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = serializers.CardSerializer


# Коллекция пользователя
class UserCollection(APIView):
    def get(self, request, user_id):
        cards = serializers.CardSerializer(User.objects.get(pk=user_id).collection_cards, many=True)
        return Response(cards.data)

    def post(self, request, user_id, card_id):
        if len(CardInUserCollection.objects.filter(user_id=user_id, card_id=card_id)) > 0:
            return Response({"res": "already in collection"})

        CardInUserCollection.objects.create(user_id=user_id, card_id=card_id)
        return Response({"res": "added"})

    def delete(self, request, user_id, card_id):
        CardInUserCollection.objects.filter(user_id=user_id, card_id=card_id).delete()
        return Response({"res": "deleted"})

class TegsListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer