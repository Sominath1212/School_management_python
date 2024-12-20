from tkinter import *
from tkinter import messagebox
from pymongo import *

h1=("Arial",15,"bold")
h2=('Arial',10,"bold")

def find_record1(q):
     try:
       con=MongoClient("localhost",27017)
       school=con['school']
       student=school['student']
       result=student.find_one(q)
       if result != None:
           con.close()
           return True
           
       else:
           return False
       
     except:
        print("something is wrong")
        con.close()
        return True

def signup():
                
                
                     
        signuppage=Tk()
        signuppage.title("Sign Up page")
        signuppage.geometry('500x500')

        Heading=Label(signuppage,text="Wel come to school",fg="red",font=h1)
        Heading.pack()
        #username
        Username=Label(signuppage,text="Username")
        Username.pack()
        Usernameinput=Entry(signuppage)
        Usernameinput.pack()
        #email
        email=Label(signuppage,text="email")
        email.pack()
        emailinput=Entry(signuppage)
        emailinput.pack()

        password=Label(signuppage,text="Password")
        password.pack()
        passwordinput=Entry(signuppage)
        passwordinput.pack()

        signupbtn=Button(signuppage,text="Create Admin",bg='blue')
        signupbtn.place(y=180,x=200)
        loginbtn=Button(signuppage,text="Login")
        loginbtn.place(y=230,x=220)


        exit=Button(signuppage,text="exit", bg="red",command=signuppage.destroy)
        exit.place(y=10,x=450)
        signuppage.mainloop()
signup()
