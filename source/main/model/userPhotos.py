from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from source import db

class UserPhotos(db.Model):
    __tablename__ = 'UserPhotos'
    PhotoID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'))
    PhotoURL = db.Column(db.String(255), nullable=False)
    UploadTime = db.Column(db.DateTime, default=db.func.current_timestamp())
    SetAsAvatar = db.Column(db.Boolean, default=False)

