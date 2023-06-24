#env
import os
# from dotenv import load_dotenv
import db
#my modules
from flask import Flask,jsonify,request,Response

# from bson import json_util
# from bson.objectid import ObjectId
import json
from flask_cors import CORS


#mqtt


#my configuration
# load_dotenv()
app=Flask(__name__)
CORS(app)

#connetion to mongodb
# app.config['MONGO_SERVER_SELECTION_TIMEOUT_MS'] = 1000 
# MongoURL=os.getenv('URL_DATABASE_LOCAL')
# MongoURC=os.getenv('URL_DATABASE')
# mongo=db.DB(MongoURC,MongoURL,app)

#api routes
@app.route('/',methods=['GET'])
def welcome():
     return "jajaj"
     
# @app.route('/movies',methods=['GET'])
# def getMovies():
#      data=mongo.getALL('Movie')
#      return Response(data,mimetype="application/json")
    
# @app.route('/movies',methods=['POST'])
# def insertMovies():
#      data=mongo.insert('Movie',{'title':request.form['title'],'year':request.form['year']})
#      return data
      
# @app.route('/movies/<id>',methods=['DELETE'])
# def deleteUser(id):
#      data=mongo.delete('Movie',{'_id':ObjectId(id)})
#      return data


# @app.route('/movies/<id>',methods=['PUT'])
# def updateMovies(id):
#      print(id)
#      # print(request.json)
#      data=mongo.update('Movie',{'title':'prueba2'},{'_id':ObjectId(id)})
#      return data
      

# @app.route('/movies/<_id>',methods=['GET'])
# def getOne(_id):
#      data=mongo.getOne('Movie',{'_id':ObjectId(_id)},{'title':1,'year':1})
#      return data