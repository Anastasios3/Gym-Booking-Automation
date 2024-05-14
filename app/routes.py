from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import BookingForm
from app.models import User
from app.scheduler import schedule_booking

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookingForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data,
                    booking_time=form.booking_time.data, system_open_date=form.system_open_date.data)
        db.session.add(user)
        db.session.commit()
        schedule_booking(user)
        flash('Booking scheduled successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
