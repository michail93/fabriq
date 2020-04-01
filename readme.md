### Разворачивание приложения
из директории в которой раходится manage.py запустите команду
```
docker-compose up
```
приложение и бд работают на 8000 и 5432 портах
### Создание пользователя
Обращения к api происходит с использванием TokenAuthentication.

Для того чтобы создать пользователя отправьте POST запрос на url /api/create-user/ со следующим JSON
```
{
    "username": "<str>",
    "password": "<str>"
}
```
в ответ будет отправлен токен соданного пользователя
 ```
{
    "user_token": "<str>"
}
```
### Получение токена ранее созданного пользователя
Для того чтобы получить токен ранее созданного пользователя отправьте следующий JSON
```
{
    "username": "<str>",
    "password": "<str>"
}

```
в ответ будет отправлен токен ранее соданного пользователя
 ```
{
    "user_token": "<str>"
}
```

### Обращения к api
* Обращние к api позволяется только с использованием токена пользователя(HTTP зголовок Authorization)
```
Authorization: Token <str>
```

* Создание приложения происходит методом POST по url /api/apps/ со следующим  JSON
```
{
	"ID": "<str>", 
	"name": "<str>"
}
```
* Получение информации о приложении происходит методом GET по url /api/apps/pk/
где pk - id(pk) приложения
* Обновление приложения происходит методами PUT и PATCH по по url /api/apps/pk/
где pk - id(pk) приложения со следующим JSON
```
{
	"ID": "<str>", 
	"name": "<str>"
}
```
* Удаление приложения происходит методом DELETE по url /api/apps/pk/
где pk - id(pk) приложения

* Получение всей информации о приложении(в том числе и Ключа API) происходит по url /api/test/api_key/ где api_key -
ключ api созданного приложения
* Получить и установить ключ api можно при помощи метода create_api_key модели Application