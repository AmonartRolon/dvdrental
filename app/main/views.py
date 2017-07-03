from flask import render_template, redirect, url_for, session, flash
from app.main import main
from datetime import datetime
from app.main.forms import NameForm
from app import db
from app.auth.models import User, Permission
from app.films.models import Film
from app.auth.decorators import admin_required, permission_required
from flask_login import login_required, current_user
from app.main.agentcomm import read_line, send_buffer, active_open

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

@main.route('/rent/<int:id>')
@login_required
def rent(id):
    message = ""
    film = Film.query.filter_by(id = id).first()
    if film is None:
        flash('Invalid film.')
        return redirect(url_for('main.index'))
    current_user.rent(film)
    flash('The film will be sended to you by mail.')
    client_socket = active_open('localhost', 4000)
    film_category = film.categories.first();
    message += str(film_category.category_id) + " "
    for f in current_user.rents.all():
        message += str(f.id) + " "

    send_buffer(client_socket, message.encode('utf-8'), len(message))
    rec = read_line(client_socket)
    client_socket.close()

    l = [int(i) for i in rec.split()]
    films = []
    for i in l:
        f = Film.query.filter_by(id = i).first()
        if f is not None:
            films.append(f)

    return render_template('/main/recommender.html', films = films);

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
