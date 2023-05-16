from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Question(db.Model):
    # Объявляем столбцы для таблицы 'question'
    id = db.Column(db.Integer, primary_key=True)  # ID вопроса
    question = db.Column(db.String, nullable=False)  # Текст вопроса
    answer = db.Column(db.String, nullable=False)  # Текст ответа
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Дата создания вопроса

    # Метод для форматирования экземпляра класса Question в словарь для отправки в виде JSON
    def format(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at
        }


def setup_db(app):
    # Задаем путь к базе данных
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@db/quiz_db'
    # Присоединяем экземпляр SQLAlchemy к нашему приложению Flask
    db.init_app(app)
    with app.app_context():
        # Создаем все таблицы
        db.create_all()
