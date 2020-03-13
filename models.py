from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    user_name = db.Column(db.String(50))
    email = db.Column(db.String(255), unique=True, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, last_name, username, email, admin):
        self.name = name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.admin = admin

    def __repr__(self):
        return '<id {}>'.format(self.user_id)
