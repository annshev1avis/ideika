from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View



def index(request): #HttpRequest
    return HttpResponse("this is ideika API!")


"""пока что обрабочики не выполняют задуманный функционал, но работают"""
class CardsView(View):
    def get(self, request):
        return HttpResponse(f"all cards")
    def post(self, request):
        return HttpResponse("create new card")


class CardsIdView(View):
    def get(self, request, card_id):
        return HttpResponse(f"get card {card_id}")

    def put(self, request, card_id):
        return HttpResponse(f"update card {card_id}")

    def delete(self, request, card_id):
        return HttpResponse(f"delete card {card_id}")


def add_card_to_collection(request, user_id, card_id):
    return HttpResponse(f"add card {card_id} to user's {user_id} collection")
