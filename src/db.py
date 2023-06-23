#modules
from flask_pymongo import PyMongo
from bson import json_util
from pymongo.errors import AutoReconnect,ConnectionFailure,ConfigurationError,ServerSelectionTimeoutError,NetworkTimeout,ExecutionTimeout

class DB:
    def __init__(self,urlDBC,urlDBL,app):
        self.URLlocal=urlDBL
        self.URLcloud=urlDBC
        self.app=app

    #method check if there is conection with local and  cloud db
    def connect(self):
        dbConnections={}
        #check if there  is conenction with mongo db Atlas 
        try:
          db1=PyMongo(self.app,uri=self.URLcloud)
          dbConnections['db1']=db1.db
        except (AutoReconnect,ConnectionFailure,ConfigurationError,ServerSelectionTimeoutError,ExecutionTimeout) as e:
          dbConnections['db1']=False
        
        #check if there is connection wit local mongo db
        try:
            db2=PyMongo(self.app,uri=self.URLlocal)
            dbConnections['db2']=db2.db
        except  (AutoReconnect,ConnectionFailure,ConfigurationError,ServerSelectionTimeoutError,NetworkTimeout,ExecutionTimeout) as e:
            dbConnections['db2']=False
            print("Error de conexión con MongoDB: {e}")

        return dbConnections
    
    #method to restore db when the connection come back 
    def  restore(self):
        dbs=self.connect()
        print("function is working from class")
        print(dbs)
    
    def command(self,collec,nosqlC,data,condition={}):
        try:
            dbs=self.connect()
            condition=data if condition == {} else condition
            if dbs['db1']!=False and dbs['db2'] != False:
                 results = {
                    result1:getattr(dbs['db1'][collec],nosqlC)(condition,data),
                    result2:getattr(dbs['db2'][collec],nosqlC)(condition,data)
                 }
                 return results
            elif dbs['db1']!=False:
                results=getattr(dbs['db1'][collec],nosqlC)(condition,data)
                return results
            elif dbs['db2'] != False:
                 results=getattr(dbs['db2'][collec],nosqlC)(condition,data)
                 return results
            else:
                return {'message':'lost connection'}
        except ServerSelectionTimeoutError as e:
            print(e)
            return {'message':'lost connection'}




    def getALL(self,collec):
       data=self.command(collec,'find',{})
       return json_util.dumps(data)
       
    
    def insert(self,collec,data):
        data=self.command(collec,'insert_one',data)
        return {"result":"insert sucessfully"}
    
    def update(self,collec,change,where):
        data=self.command(collec,'update_one',{"$set":change},where)
        return {"result":"update sucessfully"}
    
    def getOne(self,collec,where,data):
        data=self.command(collec,'find_one',data,where)
        return json_util.dumps(data)

    def delete(self,collec,where):
        dbs=self.command(collec,'delete_one',{},where)
        return {'message': 'Deleted Successfully'}


    




