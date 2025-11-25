from app import db

from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nameusers = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pass_field = db.Column("pass", db.String(255), nullable=False)  # cột 'pass'
    requestpass = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
