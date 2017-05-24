from app import db

class Film(db.Model):

    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = False)
    release_year = db.Column(db.Text, nullable = False)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    rental_duration = db.Column(db.Integer, nullable = False)
    rental_rate = db.Column(db.Numeric, nullable = False)
    length = db.Column(db.Integer, nullable = False)
    replacement_cost = db.Column(db.Numeric, nullable = False)
    rating = db.Column(db.Text)
    last_update = db.Column(db.TIMESTAMP, nullable = False)
    special_features = db.Column(db.Text)
    fulltext = db.Column(db.Text)

    def __repr__(self):
        return "<Title: {0} Description: {1} \
            Release Year: {2}>".format(self.title, self.description, self.release_year)