from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Quiz
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        question = request.form.get('question')
        answer1 = request.form.get('answer1')
        answer2 = request.form.get('answer2')
        answer3 = request.form.get('answer3')
        answer4 = request.form.get('answer4')

        if len(question) < 2:
            flash('Quiz is too short!', category='error')
        else:
            new_quiz = Quiz(question=question, user_id=current_user.id, answer1=answer1, \
            answer2=answer2, answer3=answer3, answer4=answer4)
            db.session.add(new_quiz)
            db.session.commit()
            flash('Quiz added successfully', category='success')

    no_questions = 0
    return render_template("home.html", user=current_user, no_questions=no_questions)

@views.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/credentials', methods=['GET'])
@login_required
def credentials():
    return render_template("credentials.html", user=current_user)


@views.route('/delete-quiz', methods=['POST'])
def delete_note():
    quiz = json.loads(request.data)
    quizId = quiz['quizId']
    quiz = Quiz.query.get(quizId) # find quiz by primary key
    if quiz: # if a quiz was found
        if quiz.user_id == current_user.id: # if the quiz belongs to the current user
            db.session.delete(quiz)
            db.session.commit()
    
    return jsonify({})
