import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String(50), nullable=False)
    last_name = sa.Column(sa.String(50), nullable=False)
    email = sa.Column(sa.String(100), nullable=False, unique=True)
    user_name = sa.Column(sa.String(50), nullable=False, unique=True)
    password = sa.Column(sa.String(50), nullable=False, unique=True)
