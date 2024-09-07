from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.renderers import JSONRenderer

from .models import Category, Card, Tag
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CardSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tags = SlugRelatedField(slug_field='name', many=True, read_only=True)
    users_like = SlugRelatedField(slug_field='id', many=True, read_only=True)
    description = serializers.CharField(allow_blank=True)
    
    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'create_date', 'category', 'creator', 'tags', 'users_like')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id','first_name')
