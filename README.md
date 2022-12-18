# Проектная работа 9 спринта

### Сервис авторизации

Тесты запускаются по умолчанию вместе с проектом, расположены в папке tests.
В тестах присутствуют все запросы, может служить описанием проекта.

При запуске создается суперюзер admin/admin.

## MongoDB + FastAPI
В проект добавлен MongoDB. Действия пользователя, такие как комментарии, лайки,
записываются в MongoDB

Пример POST-запроса от пользователя, чтобы поставить фильму лайк

Без access_token, мы будем получать код 401 unauthorized при обращении к адресам FastAPI

``` 
curl -X 'POST' \
  'http://localhost/api/v1/events/rating/rating_event?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MTM5MDQxOCwianRpIjoiYjZiZGY0OGYtM2E5MS00ZDllLThjZGQtYTRmMmI2MjNkNDY0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImMyN2VhZDEzLWZmOGMtNDY4My05YjY5LTUxMThhZmY0MmU0YyIsIm5iZiI6MTY3MTM5MDQxOCwiZXhwIjoxNjcxMzkwNDc4fQ.QkLGSIfyLGK35JI2gBV8FHbKZeopqXdJQXLWMJLr3Tc"' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "film_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "rating": 0
}'
```

##### Запуск проекта 

docker-compose up

**Перезапуск проекта**

1. docker-compose down
2. docker image prune --all


### Ссылка на репозиторий

https://github.com/efgraph/ugc_sprint_2
