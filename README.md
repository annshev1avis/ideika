# API для соцсети "Идейка"
Для чего: это приложение для обмена идеями, как интересно провести 
свободное время, похожее по 
принципу использования на Pinterest. В Идейке пользователи так же просматривают 
карточки (пины), добавляют понравившиеся к себе в коллекцию и могут создавать карточки сами. 
А главное отличие -- это то, что в карточках в Идейке нет фотограции: они состоят только из 
названия, описания, категории и тегов<br>
Таким образом, пользователи могут находить для себя интересные фильмы, книги, места для прогулок
и т. д. <br>
Технологии, которые применяются в проекте: <br>
- python
- Django REST Framework
- sqlite3

Кем создан: Анна Шевченко
---
## Документация 
Для передачи данных используется формат JSON<br>

Регистрация: <br>
- POST v1/auth/users/ (тело: {"username": str, "password": str} -- данные пользателя заносятся в базу 
данных

Авторизация: <br>
- POST /v1/auth/token/login/ (тело: {"username": str, "password": str}) -- если пара username-password есть в базе
данных, в ответ отправляется токен: {"auth_token": token}

Запросы, доступные без авторизационного токена: <br>
Категории карточек <br>
- GET v1/categories/ -- возвращает все категории
- GET v1/categories/<int:category_id>/ -- возвращает категорию с id = category_id
Карточки: <br>
- GET v1/cards/ -- возвращает все карточки
- GET v1/cards_by_cat/<int:category_id>/ -- возвращает все карточки, принадлежащие категории c id = category_id
- GET v1/cards/<int:card_id>/ -- возвращает карточку с id = card_id

Запросы, доступные авторизованным пользователям: <br>
(в заголовках этих запросов обязательно должен быть заголовок {"Authorization": token_str}) <br>
- POST v1/cards/ (тело: {"name": str, "description": str, "category": str}) - создание карточки
- GET v1/users/<int:user_id>/cards/ -- возвращает все карточки из коллекции пользователя с id = user_id
- POST v1/users/<int:user_id>/cards/<int:card_id>/ -- добавляет карточку с id = card_id в коллекцию пользователя с id = user_id
- DELETE v1/users/<int:user_id>/cards/<int:card_id>/  -- удаляет карточку с id = card_id из коллекции пользователя с id = user_id
- GET v1/auth/users/me/ -- информация о пользователе в формате {"email": str, "id": int, "username": str}

Запросы к отдельной карточке, доступные только ее создателю: <br>
- GET v1/cards_by_creator/<int:user_id>/ -- возвращает все карточки, которые были созданы пользователем с id = user_id

