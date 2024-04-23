from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from api.models import Card, User, CardInUserCollection, Category
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, CardSerializer, UserSerializer

class CategoryView(APIView):
    def get(self, request): # request: <rest_framework.request.Request: GET '/v1/cats/'>
        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)
        # Response умеет преобразовывать сериализованные данные в JSON

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data) # данные, которое были возвращены create()


class CardsView(APIView):
    def get(self, request):
        if(request.GET.get("categories_ids", None) is None):
            return self.all_cards()
        else:
            return self.cards_in_category(request.GET["categories_ids"])

    def all_cards(self):
        cards = Card.objects.all()
        return Response(CardSerializer(cards, many=True).data)

    def cards_in_category(self, category_ids):
        category_ids = list(map(int, category_ids.split(',')))
        cards = Card.objects.filter(category_id__in=category_ids)
        return Response(CardSerializer(cards, many=True).data)


class OneCardView(APIView):
    def get(self, request, card_id):
        try:
            card = Card.objects.get(pk=card_id)
            return Response(CardSerializer(card).data)
        except:
            return Response()

    def patch(self, request, card_id):
        try:
            card = Card.objects.get(pk=card_id)
            card.category_id = request.data["category_id"]
            card.save()
            return Response(CardSerializer(card).data)
        except:
            return Response()


class UserView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        return Response(UserSerializer(user).data)
