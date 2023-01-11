from . import db
from flask_login import UserMixin

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    no_questions = db.Column(db.Integer)
    question = db.Column(db.String(100))
    no_answers = db.Column(db.Integer)
    answer1 = db.Column(db.String(50))
    answer1_is_correct = db.Column(db.Boolean)
    answer2 = db.Column(db.String(50))
    answer2_is_correct = db.Column(db.Boolean)
    answer3 = db.Column(db.String(50))
    answer3_is_correct = db.Column(db.Boolean)  
    answer4 = db.Column(db.String(50))
    answer4_is_correct = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    quizzes = db.relationship('Quiz')