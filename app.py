from flask import Flask, request, jsonify, abort
from models import db, Question, setup_db
import requests
from datetime import datetime

app = Flask(__name__)
setup_db(app)


@app.route('/api/questions', methods=['POST'])
def get_question():
    # Загружаем данные из запроса POST
    data = request.json
    # Извлекаем количество вопросов из данных запроса
    questions_num = data.get('questions_num')

    if not questions_num or not isinstance(questions_num, int) or questions_num <= 0:
        abort(400, description="questions_num must be a positive integer.")

    # Создаем список для хранения уникальных вопросов
    unique_questions = []

    # Цикл будет выполняться до тех пор, пока количество уникальных вопросов не достигнет заданного количества
    while len(unique_questions) < questions_num:
        try:
            # Получаем случайный вопрос из внешнего API
            response = requests.get('https://jservice.io/api/random?count=1')
            # Преобразуем ответ из JSON в Python объект
            data = response.json()[0]
            response.raise_for_status()
        except requests.RequestException:
            abort(503, description="Unable to get data from external API.")

        # Извлекаем данные из ответа API
        question_id = data.get('id')
        question = data.get('question')
        answer = data.get('answer')
        created_at = datetime.now()

        # Проверяем, существует ли уже такой вопрос в базе данных
        if not Question.query.get(question_id):
            # Если вопроса нет в базе данных, создаем новый объект Question и добавляем его в базу
            new_question = Question(id=question_id, question=question, answer=answer, created_at=created_at)
            db.session.add(new_question)
            db.session.commit()
            # Добавляем новый вопрос в список уникальных вопросов
            unique_questions.append(new_question)

    # Возвращаем список уникальных вопросов в формате JSON
    return jsonify([question.format() for question in unique_questions])


@app.route('/api/questions', methods=['GET'])
def print_questions():
    # Извлекаем все вопросы из базы данных
    questions = Question.query.all()

    # Выводим каждый вопрос в консоль
    for question in questions:
        print(f"ID: {question.id}, Question: {question.question}, Answer: {question.answer}")

    # Возвращаем все вопросы в формате JSON в ответ на GET-запрос
    return jsonify([question.format() for question in questions])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
