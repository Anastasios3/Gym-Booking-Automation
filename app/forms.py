from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class BookingForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    booking_time = StringField('Desired Booking Time (24h format HH:MM)', validators=[DataRequired()])
    system_open_date = StringField('System Open Date (DD/MM/YYYY)', validators=[DataRequired()])
    submit = SubmitField('Start Booking')
