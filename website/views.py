from flask import Blueprint, flash, render_template, request, jsonify
from flask_login import login_required, current_user
import json
from website.models import History
from .translate import translate_it
from . import db
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        input_lang = request.form.get('input_lang')
        output_lang = request.form.get('output_lang')
        if len(input_text) < 1:
            flash('Text is too short.', category='error')
        else:
            words = translate_it(input_text, input_lang, output_lang)
            words = str(words)
            new_history = History(data=words, user_id=current_user.id)
            db.session.add(new_history)
            db.session.commit()
            return render_template('translated.html', words=words, user=current_user)
    return render_template('home.html', user=current_user)


@views.route('/history',)
@login_required
def history():
    return render_template('history.html', user=current_user)


@views.route('/about-us',)
def aboutus():
    return render_template('aboutus.html', user=current_user)


@views.route('/delete-history', methods=['POST'])
def delete_history():
    history = json.loads(request.data)
    historyId = history['HistoryId']
    history = History.query.get(historyId)
    if history:
        if history.user_id == current_user.id:
            db.session.delete(history)
            db.session.commit()

    return jsonify({})
