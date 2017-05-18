from app import db

class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable = False)
    last_update = db.Column(db.TIMESTAMP, nullable = False)

    def __repr__(self):
        return "<Name: {0}>".format(self.name)
