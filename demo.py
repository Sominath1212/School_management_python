from pymongo import *

def db_connection():
    try:
       con=MongoClient('localhost',27017) 
       school=con['school']
       student=school['student']
       result=list(student.find({}))
       
       i=0
       while i < len(result):
           print(result[i]['_id'],result[i]['name'],result[i]['dob'],result[i]['gender'],result[i]['email'],result[i]['mobile'],result[i]['address'])
           print()
           
           i=i+1
           
    except:
        print("something is wrong!")
        con.close()
db_connection()
        
        