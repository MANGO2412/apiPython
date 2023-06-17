#my modules
from flask import Flask,jsonify,request,Response
from flask_pymongo import PyMongo
from bson import json_util
#my configuration
app=Flask(__name__)
app.config['MONGO_URI']="mongodb://127.0.0.1:27017/cinema"

mongo=PyMongo(app)
#api routes
@app.route('/',methods=['GET'])
def welcome():
    movies=mongo.db.Movie.find()
    response=json_util.dumps(movies)
    return Response(response,mimetype="application/json")