# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:13:40 2020

@author: Ronin
"""
from flask import Flask

from .models import DB, User, add_test_users

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    DB.init_app(app)
    
    @app.route('/')
    def root():
        return'Hello, twittoff!'
        

    @app.route('/add_test_users')
    def add_users():
        DB.dropall()
        DB.create_all()
        add_test_users()
        return ('Users added!')
    
    @app.route('/view_test_users')
    def view_users():
        users = User.query.all()
        return '\n'.join([str(user) for user in users])
    
    return app