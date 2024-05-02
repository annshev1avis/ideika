from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.renderers import JSONRenderer

from .models import Category, Card, User, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CardSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='id', queryset=Category.objects.all())
    tags = SlugRelatedField(slug_field='name', many=True, read_only=True)
    users_like = SlugRelatedField(slug_field='id', many=True, read_only=True)
    
    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'create_date', 'category', 'creator', 'tags', 'users_like')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
