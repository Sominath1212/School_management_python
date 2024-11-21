from pymongo import *

def db_connection():
    try:
       con=MongoClient('localhost',27017) 
       school=con['school']
       student=school['student']
       result=student.find({})
       for student in result:
           print(student) 
    except:
        print("something is wrong!")
        con.close()
db_connection()
        
        