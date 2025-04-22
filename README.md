<h2>Автотесты на API проекта «Битва покемонов»</h2>

> **Статус проекта:**
> 🟢 Активный. Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.ru/

## Задачи проекта и описание:
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Какие тест-кейсы автоматизировал:
* Создание покемона `POST /pokemons`
* Смена имени покемона `PUT /pokemons`
* Поймать покемона в покебол `POST /trainers/add_pokeball`
* Проверить ответ метода `GET /trainers`

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе приходит корректное поле id в json

## Реализация:

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests
![image](https://github.com/ValeryQA1911/Requests-Pytest-Atests/blob/main/static/Done.png)
![image](https://github.com/ValeryQA1911/Requests-Pytest-Atests/blob/main/static/main_pok.png)

## Как запустить локально:
1. Скачать проект
2. Перейти в директорию проекта используя терминал
2. Выполнить команды:

Создать виртуальное окружение внутри папки проекта.
1. Инструкция для windows: https://realpython.com/python-virtual-environments-a-primer/#create-it\

2. Инструкция для mac

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

4. Установить библиотеки

``` markdown
python3 -m pip install requests
```

``` markdown
python3 -m pip install pytest
```
5. Перейти во вкладку testing

6. Запустить
``` markdown
pytest tests/test_pokemon.py
```

Ожидаемый результат: отчет о прохождении тестов.
![image](https://github.com/ValeryQA1911/Requests-Pytest-Atests/blob/main/static/Done.png)
