from flask import render_template, redirect, url_for, session, flash
from app.main import main
from datetime import datetime
from app.main.forms import NameForm
from app import db
from app.auth.models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))
    return render_template('/main/index.html',
            current_time = datetime.utcnow(),
            form = form, name = session.get('name'))
