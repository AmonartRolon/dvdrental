from flask import Blueprint, render_template, redirect, url_for, session, flash
from app import app
from datetime import datetime
from app.main.forms import NameForm

mod = Blueprint('app', __name__, url_prefix = '/')

@mod.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('app.index'))
    return render_template('/main/index.html',
            current_time = datetime.utcnow(),
            form = form, name = session.get('name'))
