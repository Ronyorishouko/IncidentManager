# Маленький API для учета инцидентов

> простейшая реализация с одним эндпоинтом

## Feature

- Регистрация инцидента
- Просмотр инцидентов
- Фильт по статусу
- Удаление инцидента
- Изменение инцидента

## Требования
Docker-compose==1.29.2
requirements.txt

## Установка и запуск
1. Клонировать репо на машину
2. Перейти в папку IncidentManager
3. Создать .env файл по примеру env.bak
4. Выполнить команду docker-compose up --build
5. Сервис будет доступен по адресу http://localhost:8000/api/


## Пример использования

#### GET http://localhost:8000/api/incidents/
> получить список инцидентов JSON

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "description": "asd",
            "status": "open",
            "source": "operator",
            "created_at": "2025-11-08T05:32:41.295730+03:00"
        }
    ]
}
```

#### POST http://localhost:8000/api/incidents/ 
> body:{"description": "","source": ""} \
> где description - описание проблемы; source - источник (operator\monitoring\system)

Создать инцидент.
Ответ при успешном создании 201.

#### GET http://localhost:8000/api/incidents/1/
> Информация по конкретному инциденту


#### PATCH http://localhost:8000/api/incidents/1/
> body:{"description": "", "status": "", "source": ""}

Изенение данных по инциденту.

#### DELETE http://localhost:8000/api/incidents/1/
Удалить инцидент


#### PATCH http://localhost:8000/api/incidents/1/update_status/
> body:{"status": ""}

Эндпоинт в котором разрешено менять только статус


#### GET http://localhost:8000/api/incidents/?status=open
> получить список инцидентов JSON с фильтром по статусу
