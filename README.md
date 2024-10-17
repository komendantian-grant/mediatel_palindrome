# Сервис для генерации палиндромов
Веб-сервис для генерации палиндромов за наименьшее количество перестановок.

На вход сервиса поступает строка в json. 
После этого сервис пытается получить из строки палиндром за наименьшее количество перестановок любых символов.
Кроме того, из возможных вариантов выбирается минимальный лексикографически палиндром.
На выход подается json со строкой palindrome и результатом.
Если из строки невозможно получить палиндром, на выход подаётся null.

Сервис находится в Docker-контейнере. 
После клонирования репозитория сервис поднимается с помощью команды: 
```commandline
docker compose up
```

Сервис написан с использованием FastAPI.
По умолчанию сервис запускается на localhost на порте 80.

Обработка строки производится с помощью модуля make_palindrome. 
Для основной функции make_palindrome написаны юнит-тесты, проверяющие ряд простых случаев трансформации.

Пример запроса к сервису:
```commandline
curl -X POST 127.0.0.1:80 -H 'Content-Type: application/json' -d '{"word":"abcabc"} -v'
```
Результат выполнения запроса:
```commandline
< HTTP/1.1 200 OK
< date: Thu, 17 Oct 2024 15:27:56 GMT
< server: uvicorn
< content-length: 23
< content-type: application/json
< 
* Connection #0 to host 127.0.0.1 left intact
{"palindrome":"abccba"}
```
Пример запроса со строкой, не превращаемой в палиндром:
```commandline
curl -X POST 127.0.0.1:80 -H 'Content-Type: application/json' -d '{"word":"aaabbb"} -v'
```
Результат выполнения запроса:
```commandline
< HTTP/1.1 200 OK
< date: Thu, 17 Oct 2024 15:30:09 GMT
< server: uvicorn
< content-length: 19
< content-type: application/json
< 
* Connection #0 to host 127.0.0.1 left intact
{"palindrome":null}
```