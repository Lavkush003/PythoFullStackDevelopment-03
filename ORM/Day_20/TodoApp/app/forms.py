
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TodoForm(FlaskForm):
    task = StringField(
        "Task",
        validators=[DataRequired(), Length(min=1, max=380)]
    )
    submit = SubmitField("Save")
