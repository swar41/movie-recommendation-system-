# app/routes.py
from flask import render_template, request
from app import app
from models.model import get_recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie1 = request.form.get('movie1')
    movie2 = request.form.get('movie2')
    movie3 = request.form.get('movie3')
    preferences = [movie1, movie2, movie3]
    recommendations = get_recommendations(preferences)
    return render_template('index.html', recommendations=recommendations)
