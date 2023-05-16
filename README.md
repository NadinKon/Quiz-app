## Quiz-app 
Сервис принимающий на вход запросы с содержимым вида {"questions_num": integer}.
После получения запроса, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов и сохраняет уникальные в bd.


### Установка и запуск:
Клонируйте репозиторий и перейдите в рабочую директорию

git clone https://github.com/NadinKon/Quiz-app <br>

cd Quiz

### Соберите образы Docker Compose и запустите контейнеры:
docker-compose up -d --build

### Использование:
Приложение теперь запущено и доступно по адресу http://localhost:5000

### Пример POST-запроса:
Для получения уникальных вопросов отправьте POST-запрос на http://localhost:5000/api/questions с телом запроса вида {"questions_num": integer}. <br>
Например: curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 5}' http://localhost:5000/api/questions

Пример запроса через Powershell Windows:
Invoke-WebRequest -Uri http://localhost:5000/api/questions -Method POST -ContentType "application/json" -Body '{"questions_num":3}'

Для получения всех вопросов из базы данных отправьте GET-запрос на http://localhost:5000/api/questions. <br>
Например: curl -X GET http://localhost:5000/api/questions

### Остановка и удаление контейнеров:
Чтобы остановить и удалить контейнеры, выполните следующую команду: <br>
docker-compose down

Все данные сохраняются в Docker volume, это означает, что данные сохраняются даже при остановке и удалении контейнеров. <br>
Если вам нужно удалить volume и все его данные, выполните следующую команду: <br>
docker volume rm your_repository_dbdata


*Made with Flask and SQLAlchemy
