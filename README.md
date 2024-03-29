# api_yamdb

## _**Описание**_

Групповой проект API YaMDb. Социальная сеть, в которой хранятся
произведения (книги, фильмы или музыка) с возможностью оставить отзыв.

## _**Установка**_

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/GandraNNA/api_yamdb.git
```

```
cd api_yamdb
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

В PyCharm активировать виртуальное окружение в терминале можно так:

```
.\venv\Scripts\activate.ps1
```

### Обновить pip:

```
python -m pip install --upgrade pip
```

### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
python manage.py migrate
```

### Запустить проект:

```
python manage.py runserver
```

## _**Некоторые примеры запросов.**_

Можно поcмотреть после установки проекта по ссылке:
http://127.0.0.1:8000/redoc/

### _**Авторы:**_

- _**Эльтун Гасимов - https://github.com/gasimovv21**_
- _**Артём Выжимов - https://github.com/ArtemVyzhimov**_
- _**Анна Гандрабура - https://github.com/GandraNNA**_
