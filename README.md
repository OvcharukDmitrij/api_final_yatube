# Привет! 
Меня зовут Овчарук Дмитрий, я ученик 17 когорты
Яндекс.Практикума и я автор этого сайта!

Это мой первый проект и первый опыт в программировании,
поэтому прошу относиться к сайту снисходительно))))

Сайт будет улучшаться и развиваться. Если ты хочешь поучаствовать в этом,
то присылай свои предложения мне.

Мои контакты:

ovcharukdmitrij@ya.ru

github.com/OvcharukDmitrij
### Описание

Сайт YATUBE является социальной сетью,
позволяющей авторизированным пользователям вести собственный дневник и делать в нем записи совершенно
на любую тему, а анонимным пользователям просматривать существующие записи.

В рамках проекта использовались следующие технологии:

#### Python
#### Django
#### SQLite3
#### HTML
#### API DRF
#### GitHub
#### и сотни страниц с информацией в интернете)))

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

### Права доступа к эндпоинтам.
У неаутентифицированных пользователей имеется доступ к API только на чтение.

Доступ к эндпоинту /api/v1/follow/ предоставляется только аутентифицированным пользователям.

Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

Для аутентификации необходимо получить токен сделав POST запрос к эндпоинту api/v1/jwt/create передав в запросе username и password пользователя.