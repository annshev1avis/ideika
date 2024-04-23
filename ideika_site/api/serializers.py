from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.renderers import JSONRenderer

from .models import Category, Card, User

# Роль сериализатора: выполнять конвертирование произвольных объектов
# Python(модели, QuerySet) в формат JSON

"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
 """

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class CardSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(
        slug_field='name',
        queryset=Category.objects
    )
    tags = SlugRelatedField(
        slug_field='name',
        many=True,
        read_only=True
    )
    users_like = SlugRelatedField(
        slug_field='id',
        many=True,
        queryset=User.objects
    )
    class Meta:
        model = Card
        fields = ['id', 'name', 'description', 'category', 'tags', 'users_like']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'login', 'name', 'email']

def to_json():
    cat = Category(name="Shashlikoff")
    cat_ser = CategorySerializer(cat) # в словарь
    print(cat_ser.data, type(cat_ser.data), cat_ser, type(cat_ser))
    # {'id': None, 'name': 'Shashlikoff'}, dict, CategorySerializer(<Category: Shashlikoff>)

    json = JSONRenderer().render(cat_ser.data) # в JSON
    print(json, type(json))
    # b'{"id":null,"name":"Shashlikoff"}' <class 'bytes'>


# def from_json():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data) # возвратит упорядоченный словарь (объект сериализации)
#     serializer.is_valid()
#     validated_data появляется после is_valid()
#     print(serializer.validated_data) # упорядоченный словарь
