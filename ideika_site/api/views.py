from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from api.models import Card, User, CardInUserCollection
import json


def index(request): #HttpRequest
    return HttpResponse("this is ideika API!")


"""добавить сортировки: сначала новые, сначала старые, по алфавиту"""
# /cards
class CardsView(View):
    def get(self, request):

        if "collection_id" in request.GET:
            cards = Card.objects.filter(category_id=request.GET["category_id"])
        else:
            cards = Card.objects.all()

        cards_list = []
        for card in cards:
            cards_list.append({"id": card.id,
                             "name": card.name,
                             "desc": card.description,
                             "own": False})

        # добавляет информацию о том, если ли карточка в коллекции пользователя
        if "user_id" in request.GET:
            collection_ids = [c.id for c in CardInUserCollection.objects.filter(user_id=request.GET["user_id"])]
            for i in range(len(cards_list)):
                cards_list[i]["own"] =  cards_list[i]["id"] in collection_ids

        return JsonResponse(cards_list, safe=False)

    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))

        new_card = Card(name=body["name"], description=body["description"], creator_id=body["creator_id"],
                        category_id=body["category_id"])
        new_card.save()

        return HttpResponse("create new card")

# cards/4/
class CardsIdView(View):
    def get(self, request, card_id):
        return HttpResponse(f"get card {card_id}")

    def put(self, request, card_id):
        return HttpResponse(f"update card {card_id}")

    def delete(self, request, card_id):
        return HttpResponse(f"delete card {card_id}")

# users/1/cards/4
class CardUser(View):
    def get(self, request, user_id):
        cards = []
        cards_in_collection_ids = [x.id for x in CardInUserCollection.objects.filter(user_id=user_id)]
        watched_ids = [x.id for x in CardInUserCollection.objects.filter(is_watched=1)]
        for card in Card.objects.filter(id__in=cards_in_collection_ids):
            cards.append({
                "id": card.id,
                "name": card.name,
                "description": card.description,
                "watched": card.id in watched_ids
            })

        return HttpResponse(cards)

    def post(self, request, user_id, card_id):
        return HttpResponse(f"new card {card_id} for user {user_id}")


# cards/1/tags/2
class CardTag(View):
    def get(self):
        pass

