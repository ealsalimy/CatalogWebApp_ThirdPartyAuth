from flask import(Flask, render_template, request, redirect, jsonify,
                  url_for, flash, g, session as login_session)
from sqlalchemy import create_engine, desc
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, joinedload
from models import Base, Categories, Items, User
import json
from flask import make_response
import requests
import random
import httplib2
import string
import os

# Connect to Database and create database session
engine = create_engine('sqlite:///ItemCatalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

app = Flask(__name__)
DBSession = sessionmaker(bind=engine)
session = DBSession()
app.secret_key = os.urandom(32)

@app.route('/google_connect', methods=['GET', 'POST'])
def gconnect():
    # Validate state token
    if request.args.get('state', '') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    categories = session.query(Categories).all()
    items = session.query(Items).order_by(desc(Items.id)).limit(10).all()
    category_list = []
    '''
    make a list of dictionary to store the categories
    names and to be able to display the category
    name with each item
    '''
    for c in categories:
        category_list.append(dict(id=c.id, name=c.name))
    # Create anti-forgery state token
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # Build authentication link to google account
    url = 'https://accounts.google.com/o/oauth2/v2/auth?'
    url += 'client_id=354270557828-caritkd8lfe68d1bsdevphcs6i1i30qd.'
    url += 'apps.googleusercontent.com&'
    url += 'response_type=code&'
    url += 'scope=openid%20email&'
    url += 'redirect_uri=http://localhost:5000/google_connect&'
    url += 'state=%s&' % state
    return render_template('public_catalog.html', categories=categories,
                           items=items, category_list=category_list,
                           STATE=state, link=url)




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
