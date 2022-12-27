# api_final
### Описание

Сайт YATUBE является социальной сетью,
позволяющей авторизированным пользователям вести собственный дневник и делать в нем записи совершенно
на любую тему, а анонимным пользователям просматривать существующие записи.
В рамках проекта, кроме прочего, реализовано API с использованием DRF (django rest framework).

### Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:OvcharukDmitrij/api_final_yatube.git
```

```
cd kittygram
```



Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов к API

#### Получить список всех публикаций:
GET /api/v1/posts/
#### Добавление новой публикации в коллекцию публикаций:
POST /api/v1/posts/
#### Получение публикации по id.:
GET /api/v1/posts/{post_id}
#### Получение всех комментариев к публикации:
GET /api/v1/posts/{post_id}/comments/
#### Получение списка доступных сообществ:
GET /api/v1/groups/
#### Возвращает все подписки пользователя, сделавшего запрос:
GET /api/v1/follow/