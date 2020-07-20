# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:29:28 2020

@author: Ronin
"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy() 

TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
                 'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
                 'common_squirrel', 'KenJennings', 'conanobrien',
                 'big_ben_clock', 'IAM_SHAKESPEARE']

class  User(DB.Model):
    """Twitter Users"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    
    def __repr__(self):
        return'User {}'.format(self.name)
        
def add_test_users():
    for i, name in enumerate(TWITTER_USERS):
        user = User(id=i, name=name)
        DB.session.add(user)
    DB.session.commit()