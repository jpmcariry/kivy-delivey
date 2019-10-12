from flask import Flask, jsonify, session, request, redirect, url_for, g
from flask_restful import Api
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,jwt_refresh_token_required, create_refresh_token,get_jwt_identity, set_access_cookies,set_refresh_cookies, unset_jwt_cookies
from .blacklist import BLACKLIST
from datetime import timedelta
import os
import cgi
import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dawdwadwa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'fSAdfeqfdxz12xcvraw2'
app.config['JWT_BLACKLIST_ENABLED'] = True



api = Api(app)
api.add_resource(Login, "/login")
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

if __name__ == '__main__':
    from .sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
