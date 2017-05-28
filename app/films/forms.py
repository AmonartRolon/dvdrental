from flask_wtf import Form
from wtforms import SelectField, SubmitField, ValidationError
from app.categories.models import Category

class CategorySelectionForm(Form):
    category_list = SelectField(u'Category', coerce = int)
    submit = SubmitField(u'Submit')
    def __init__(self):
        super().__init__()
        self.category_list.choices = []
        self.category_list.choices.append((None, 'Choose a category'))
        self.category_list.choices = [(category.id, category.name) for category in Category.query.all()]

    def validate_category_list(self, field):
        if field.data == None:
            raise ValidationError('Select an option!')
