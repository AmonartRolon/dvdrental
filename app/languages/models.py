from app import db

class Language(db.Model):

    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    films = db.relationship('Film', backref = 'language', lazy = 'dynamic')
    last_update = db.Column(db.TIMESTAMP, nullable = False)
    films = db.relationship('Film', backref = 'language', lazy = 'dynamic')

    def __repr__(self):
        return "<Name: {0}>".format(self.name)
