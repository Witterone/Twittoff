# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:13:40 2020

@author: Ronin
"""
from os import getenvn

from flask import Flask, render_template, request

from .models import DB, User

from .predict import predict_user

from .twitter import add_or_update_user, update_all_users

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = getenvn('DATABASE_URL')
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    DB.init_app(app)
    
    
    
    @app.route('/')
    def root():
        return render_template('base.html', title = 'Home',
                               users = User.query.all())
    
    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods =['GET'])
    def user(name=None, message = ''):
        name = name or request.values['user_name']
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.name==name).one().tweets
        except Exception as e:
            message = "Error adding {}: {}".format(name, e)
            tweets = []
        return render_template('user.html', title=name, tweets=tweets,
                               message=message)
            
        
    @app.route('/compare', methods = ['POST'])
    def compare(message=''):
        user1, user2 = sorted(request.values['user1'],
                               request.values['user2'])
        if user1 == user2:
            message = "It's pointless to compare a user to themself."

        else:
            prediction = predict_user(user1, user2, 
                                      request.values['tweet_text'])
            message='"{}" is more likely to be said by {} than {}'.format(
                request.values['tweet_text'], 
                user1 if prediction else user2,
                user2 if prediction else user1
            )
        return render_template('prediction.html', title='Prediction',
                               message=message)
    
    @app.route('/add_test_users')
    def reset():
        DB.dropall()
        DB.create_all()
        return render_template("base.html", title='Reset database!')
    
    @app.route('/view_test_users')
    def update():
        update_all_users()
        return render_template("base.html", user=User.query.all(),
                               title='All users and tweets updated')
    return app