# Древовидное меню

### Описание проекта

Приложение формирующее древовидное меню на основе рекурсии

### Технологии

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/): web-фреймворк для создания backend-части приложения.
- [PostgreSQL](https://www.postgresql.org/): реляционная база данных для хранения данных.

### Начало работы

1. Установить переменные окружения:

    ```sh
    $ python3 -m venv venv
    ```

2. Создать файл .env по примеру .env_example:

    ```sh
    SECRET_KEY=...
    DEBUG=...
    ```

3. Активировать изолированную среду и установить зависимости:

    ```sh
    $ soruce venv/bin/activate (linux)
    $ pip install -r requirements.txt 
    ```

4. Сделать миграции:

    ```sh
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    ```

5. Заполнить базу данных (фикстурами):

    ```sh
    $ python3 manage.py loaddata tree_menu/fixtures.json 
    ```

---

### Зависимости:

```python
'Django==5.0.1'
'psycopg2-binary==2.9.9'
'python-dotenv==1.0.1'
'asgiref==3.7.2'
'sqlparse==0.4.4'
'typing_extensions==4.9.0'
```

---

### URL `эндпоинты`:

* `http://127.0.0.1:8000/`

---

### Функциональные возможности и описание

* Модели: `Menu` и `MenuItem` - представляют собой меню и ветки, которые формируют url из slug.
* Templatetags включает себя рекурсивное `draw_menu()`, которое формирует разметку и раскрывает текущее древо если оно
  совпадает с текущим endpont'ом.