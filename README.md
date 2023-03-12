# Api yatube

### Описание проекта

Учебный проект от ЯП.  
Api для социальной сети блогеров  
(посты, группы, комментарии, подписка, авторизация по токену jwt)

#### Примеры запросов:
GET `/api/v1/posts/`
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
POST `/api/v1/jwt/create/`
```json
{
  "username": "string",
  "password": "string"
}
```


### Технологии
- Python 3.9
- Django 3.2
- DRF 3.12
- Docker

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:GitHub-NikName/api_final_yatube.git
```

```bash
cd api_final_yatube
```

Запустить проект:


```bash
python -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt  
```
Или:


`bash
docker-compose up -d
`

подключиться к контейнеру:
`bash
docker exec -it container_name sh
`  
Выполнить миграции:
`bash
python3 manage.py migrate
`  

### Контакты:
Михаил  
[email](server-15@yandex.ru)  
[telegram](https://t.me/sergeev_mikhail)
