# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:29:28 2020

@author: Ronin
"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy() 



class  User(DB.Model):
    """Twitter Users"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Columns(DB.BigInteger)
    
    
    def __repr__(self):
        return'User {}'.format(self.name)
        
class Tweet(DB.Model):
    id =  DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger,
                        DB.ForeignKey('user.id'),nullable=False)
    user = DB.relationship('User', 
                           backref = DB.backref('tweets', lazy=True))
    
    def __repr__(self):
        return'[Tweet {}]'.format(self.text)
    
def add_test_users():
    for i, name in enumerate(TWITTER_USERS):
        user = User(id=i, name=name)
        DB.session.add(user)
    DB.session.commit()