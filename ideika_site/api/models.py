from django.db import models

class Message(models.Model):
    class Direction(models.IntegerChoices):
        TO_ADMIN = (0, 'Админу')
        TO_USER = (1, 'Пользователю')

    mes_text = models.TextField()
    direction = models.BooleanField(choices=Direction.choices, default=Direction.TO_ADMIN)
    is_watched = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

class User(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=50, unique=True, null=True)
    registrate_date = models.DateField(auto_now_add=True)

    collection_cards = models.ManyToManyField('Card', through='CardInUserCollection', related_name="users_like")

    def __str__(self):
        return self.name

class CardInUserCollection(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    is_watched = models.BooleanField(default=False)
    added_dt = models.DateTimeField(auto_now_add=True)

class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    is_banned = models.BooleanField(default=False)

    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    creator = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    tags = models.ManyToManyField('Tag', blank=True, related_name="cards")
    # users_like

    # TODO
    # прописать менеджер записей published

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
