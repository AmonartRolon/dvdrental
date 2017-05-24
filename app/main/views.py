from flask import render_template, redirect, url_for, session, flash
from app.main import main
from datetime import datetime
from app.main.forms import NameForm
from app import db
from app.auth.models import User, Permission
from app.auth.decorators import admin_required, permission_required
from flask_login import login_required

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

@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "For administrators!"

@main.route('/shop_owner')
@login_required
@permission_required(Permission.SHOP_OWNER)
def for_shop_owners_only():
    return "For shop owners only"
