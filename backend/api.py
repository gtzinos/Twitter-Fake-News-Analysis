from flask import Flask, json, Response, jsonify, request
from config.database import *
from bson.json_util import dumps
from flask_cors import CORS
from flask import request
from database.retweets import *
from database.followers import *
from database.users import *

from database.connect import *

app = Flask(__name__)
app.Debug = True

CORS(app)


@app.route("/users")
def get_users():
    db = openConnection(db_hostname, db_name, db_port, db_username, db_password, db_authMechanism)

    users = Users(users_table_name).find_all(db)

    output = []

    for user in users:
        del user['_id']
        output.append(user)
    print(output)
    return jsonify(output)


@app.route("/retweets-per-month", methods=['POST'])
def retweets_per_month():
    userId = request.get_json().get('userId')

    db = openConnection(db_hostname, db_name, db_port, db_username, db_password, db_authMechanism)

    retweets = Retweets(
        name=retweets_table_name).get_retweets_by_date(db, userId)

    output = []
    for retweet in retweets:
        retweet['id'] = retweet['_id']
        output.append(retweet)

    return jsonify(output)


@app.route("/retweets-per-hop", methods=['POST'])
def retweets_per_hop():
    userId = request.get_json().get('userId')

    db = openConnection(db_hostname, db_name, db_port, db_username, db_password, db_authMechanism)

    retweets = Followers(
        name=followers_table_name).get_tweets_by_hop(db, userId, retweets_table_name)

    output = []
    for retweet in retweets:
        retweet['id'] = retweet['_id']
        output.append(retweet)

    return jsonify(output)
