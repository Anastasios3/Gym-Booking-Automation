from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.booking import book_gym
import time

def schedule_booking(user):
    scheduler = BackgroundScheduler()
    system_open_datetime = datetime.strptime(user.system_open_date + " 03:00", "%d/%m/%Y %H:%M")
    delay_seconds = (datetime.strptime(user.system_open_date + " " + user.booking_time, "%d/%m/%Y %H:%M") - system_open_datetime).total_seconds()

    scheduler.add_job(book_gym, 'date', run_date=system_open_datetime, args=[user.email, user.password, user.booking_time], misfire_grace_time=int(delay_seconds))
    scheduler.start()
