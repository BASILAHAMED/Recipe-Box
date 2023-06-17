from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__ = 'recipes' # create database and table to store data
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
