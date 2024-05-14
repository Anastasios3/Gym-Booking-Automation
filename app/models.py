from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    booking_time = db.Column(db.String(5), nullable=False)
    system_open_date = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
