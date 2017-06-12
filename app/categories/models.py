from app import db
from app.films.models import FilmCategory

class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable = False)
    last_update = db.Column(db.TIMESTAMP, nullable = False)

    films = db.relationship('FilmCategory',
                            foreign_keys = [FilmCategory.category_id],
                            backref = db.backref('categories', lazy = 'joined'),
                            lazy = 'dynamic',
                            cascade = 'all, delete-orphan')


    def __repr__(self):
        return "<Name: {0}>".format(self.name)
