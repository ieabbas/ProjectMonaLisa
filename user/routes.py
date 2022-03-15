from flask import Flask
from app import app
from user.models import User

@app.route('/home/videocount/')
def videoCount():
    user = User('cherrius_')
    return user.getVideoCount()

