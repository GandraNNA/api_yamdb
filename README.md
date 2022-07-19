### Документация по API доступна по адресу http://localhost:8000/redoc/.

# Установка (Выполните следующие действия)

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

Активировать виртуальное окружение

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
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
python manage.py runserver
```
