from flask import Flask, render_template, session, redirect


app = Flask(__name__)

from user import routes

@app.route('/home/')
def home():
    return render_template('home.html')

