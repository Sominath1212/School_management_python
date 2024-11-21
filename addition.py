from tkinter import *
from pymongo import MongoClient 
from tkinter import messagebox
h1=("Arial",15,"bold")
h2=('Arial',10,"bold")

def find_record(q):
    try:
       con=MongoClient("localhost",27017)
       school=con['school']
       student=school['student']
       result=student.find_one(q)
       if result != None:
           con.close()
           return result
           
       else:
           return False
       
    except:
        print("something is wrong")
        con.close()
        return True

    
remove_base=Tk()
remove_base.geometry("600x600")
remove_base.title("addmission form")
heading=Label(remove_base,text="New Addmission",font=h1)
heading.place(x=200,y=50)
#name
namelabel=Label(remove_base,text="Email: ",font=h2)
namelabel.place(x=10,y=100)
nameinput=Entry(remove_base)
nameinput.configure(width=60)
nameinput.place(x=75,y=100)

def search_user():
    
    email=nameinput.get()
    if email=="":
        messagebox.showwarning(title="warnnig",message="Enter Email!")
    else:
            
      findq={"email":email}

      is_present=find_record(findq)
      if is_present:
        data=list(is_present.values())
        keys=list(is_present.keys())
        
        line0=Label(remove_base,text=f"|  {keys[0]}  | {data[0]}")
        line1=Label(remove_base,text=f"|  {keys[1]}  | {data[1]}")
        line2=Label(remove_base,text=f"|  {keys[2]}  | {data[2]}")
        line3=Label(remove_base,text=f"|  {keys[3]}  | {data[3]}")
        line4=Label(remove_base,text=f"|  {keys[4]}  | {data[4]}")
        line5=Label(remove_base,text=f"|  {keys[5]}  | {data[5]}")
        line6=Label(remove_base,text=f"|  {keys[6]}  | {data[6]}")
        dotline=Label(remove_base,text="__________________________________________")
        dotline.place(x=200,y=190)
        line0.place(x=200,y=220 )
        line1.place(x=200,y=250 )
        line2.place(x=200,y=280 )
        line3.place(x=200,y=310 )
        line4.place(x=200,y=330 )
        line5.place(x=200,y=370 )
        line6.place(x=200,y=400 )
        dotline2=Label(remove_base,text="__________________________________________")
        dotline2.place(x=200,y=430)
        remove_base.mainloop()
        
      else:
        messagebox.showinfo(title="no record",message="No such record found")
        
        
backbtn=Button(remove_base,text="Back",command=remove_base.destroy)
backbtn.configure(bg="blue")
cancel=Button(remove_base,text="Cancel" ,font=h2,command=remove_base.destroy)
cancel.configure(bg="blue")
submit=Button(remove_base,text="SEARCH" ,font=h2,command=search_user)
submit.configure(bg="blue")
backbtn.place(x=150,y=150)
cancel.place(x=200,y=150)
submit.place(x=500,y=95)
remove_base.mainloop()
