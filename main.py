from tkinter import *
from pymongo import MongoClient 
from tkinter import messagebox
from tkinter import ttk
#mongodb://localhost:27017/
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
#new addmission
def newaddmission():
    
    def postdata():
      name=nameinput.get()
      dob=DOBinput.get()
      address=addinput.get()
      mobile=mobileinput.get()
      email=Emailinput.get()
      gender=genderinput.get()
      
      if name=="" and dob==""and gender==""and address==""and email=="" and mobile=="":
          messagebox.showwarning(title="Incomplete imformation",message="please fill the all fields")
          add_form.destroy()
          add_form.mainloop()
          return
      else:   
          q={"name":name,"dob":dob, "gender":gender, "address":address,"email":email,'mobile':mobile}
          findq={"name":name,"email":email}
          is_present=find_record1(findq)
          if not is_present:
           try:
             con=MongoClient('localhost',27017)
             school=con['school']
             student=school['student']
             saved=student.insert_one(q)
             if saved.acknowledged:
               messagebox.askokcancel(title="success",message="new student added...")
               add_form.destroy()
               con.close()
               return
               
             else:
                print("record not saved")
                messagebox.showerror(title="error",message="record not saved...")
           except:
            print("connection failed...")
            con.close()
            messagebox.showerror(title="error",message=" failed to connect with the server...")
          else:
             messagebox.showinfo(title="alredy having",message="this records already have in system")   
             return add_form.destroy()

    add_form=Tk()
    add_form.geometry("600x600")
    add_form.title("addmission form")
    heading=Label(add_form,text="New Addmission",font=h1)
    heading.place(x=200,y=50)
    #name
    namelabel=Label(add_form,text="Name: ",font=h2)
    namelabel.place(x=10,y=100)
    nameinput=Entry(add_form)
    nameinput.configure(width=60)
    nameinput.place(x=75,y=100)
    
    
    #date of birth
    DOBlabel=Label(add_form,text="DOB:",font=h2)
    DOBlabel.place(x=10,y=150)
    DOBinput=Entry(add_form)
    DOBinput.configure(width=60)
    DOBinput.place(x=80,y=150)
    
    

    #address
    addlabel=Label(add_form,text="Address:",font=h2)
    addlabel.place(x=10,y=200)
    addinput=Entry(add_form)
    addinput.configure(width=60)
    addinput.place(x=80,y=200)
    

    # mobile no 
    mobilelabel=Label(add_form,text="Mobile No:",font=h2)
    mobilelabel.place(x=10,y=250)
    mobileinput=Entry(add_form)
    mobileinput.configure(width=60)
    mobileinput.place(x=80,y=250)
    

    #   email
    Emaillabel=Label(add_form,text="Email No:",font=h2)
    Emaillabel.place(x=10,y=300)
    Emailinput=Entry(add_form)
    Emailinput.configure(width=60)
    Emailinput.place(x=80,y=300)
   #gender
    Emaillabel=Label(add_form,text="Gender:",font=h2)
    Emaillabel.place(x=10,y=350)

    genderinput = Entry(add_form)
    genderinput.place(x=80,y=350)

    cancel=Button(add_form,text="Cancel" ,font=h2,command=add_form.destroy)
    cancel.configure(bg="blue")
    submit=Button(add_form,text="Submit" ,font=h2,command=postdata)
    submit.configure(bg="blue")
    cancel.place(x=200,y=400)
    submit.place(x=300,y=400)

    add_form.mainloop()


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

    
#remove student
def remove_student():    
    

 remove_base=Tk()
 remove_base.title("Remove student base")
 remove_base.geometry("600x600")
 remove_base.title("REMOVE STUDENT")
 heading=Label(remove_base,text="REMOVE STUDENT",font=h1)
 heading.place(x=200,y=50)
 #email
 namelabel=Label(remove_base,text="Email: ",font=h2)
 namelabel.place(x=10,y=100)
 nameinput=Entry(remove_base)
 nameinput.configure(width=60)
 nameinput.place(x=75,y=100)
 def remove_from_db(q):
    conform=messagebox.askyesno(title="conformation",message="Do you Want remove Student")  
    
    if conform:
        try:
             con=MongoClient("localhost",27017)
             school=con['school']
             student=school['student']
             result = student.delete_one(q)
             if result.deleted_count>0:
                 messagebox.showinfo(message="Student Deleted successfully!")
                 remove_base.destroy()
             
        except:
            print("server problem")
    else:
        remove_base.destroy()
        
 def delete_user():
    
    email=nameinput.get()
    findq={"email":email}
    def rm_db():
        remove_from_db(findq)
    is_present=find_record(findq)
    if is_present:
        data=list(is_present.values())
        keys=list(is_present.keys())
        
        delete_btn=Button(remove_base,text="Delete Student",bg="red",command=rm_db)
        delete_btn.place(x=400,y=150)
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
        
        
    
 cancel=Button(remove_base,text="Cancel" ,font=h2,command=remove_base.destroy)
 cancel.configure(bg="blue")
 submit=Button(remove_base,text="Submit" ,font=h2,command=delete_user)
 submit.configure(bg="blue")
 cancel.place(x=200,y=150)
 submit.place(x=300,y=150)
 remove_base.mainloop()
#search student
def search_student():    
    
    
    remove_base=Tk()
    remove_base.title("Search student")
    remove_base.title("Remove student")
    remove_base.geometry("600x600")
    remove_base.title("SEARCH STUDENT")
    heading=Label(remove_base,text="SEARCH STUDENT",font=h1)
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
    
    
def get_all_students():
    try:
        con=MongoClient('localhost',27017) 
        school=con['school']
        student=school['student']
        result=list(student.find({}))
        return result;
        
    except:
        print("something is wrong!")
        con.close()
def All_students():
    win = Tk()
    win.title("All students")
    win.geometry("1000x500")
    style =ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(win, column=("Id", "Name", "DOB","Gender","Email","MO NO","ADDRESS"), show='headings')
    tree.column("# 1", anchor=CENTER,width=170)
    tree.heading("# 1", text="Id")
    tree.column("# 2", anchor=CENTER,width=150)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER,width=150)
    tree.heading("# 3", text="DOB")
    tree.column("# 4", anchor=CENTER,width=150)
    tree.heading("# 4", text="Gender")
    tree.column("# 5", anchor=CENTER,width=70)
    tree.heading("# 5", text="Email")
    tree.column("# 6", anchor=CENTER,width=150)
    tree.heading("# 6", text="MONO")
    tree.column("# 7", anchor=CENTER,width=150)
    tree.heading("# 7", text="ADDRESS")
    result=get_all_students()
    if result==[]:
        Heading=Label(win,text="No such students present!",font=h1,anchor=CENTER)
        Heading.pack()
    else:
        i=0;
        while i < len(result):
            tree.insert("","end",text='1',values=(result[i]['_id'],result[i]['name'],result[i]['dob'],result[i]['gender'],result[i]['email'],result[i]['mobile'],result[i]['address']))
            i=i+1;
        Heading=Label(win,text="All students",font=h1,anchor=CENTER)
        Heading.pack()
        tree.pack()
    win.mainloop()
#dashboard
def login_function():
    base.destroy()
    dashboard=Tk()
    dashboard.title("dashboard")
    dashboard.geometry('500x500')
    Heading=Label(dashboard,text="Dash Board",fg="red",font=h1,padx = 10, pady = 10)
    Heading.place(x=200,y=40)
    addmissionbtn=Button(dashboard,text="New Admission",bg="yellow",font=h2,padx = 10, pady = 10,command=newaddmission)
    addmissionbtn.place(y=100,x=100)
    removebtn=Button(dashboard,text="remove student",bg="yellow",font=h2,padx = 10, pady = 10,command=remove_student)
    removebtn.place(y=100,x=250)
    searchstudentbtn=Button(dashboard,text="Search Student",bg="yellow",font=h2,padx = 10, pady = 10,command=search_student)
    searchstudentbtn.place(y=200,x=100)
    allstudentbtn=Button(dashboard,text="Show all students",bg="yellow",command=All_students,font=h2,padx = 10, pady = 10)
    allstudentbtn.place(y=200,x=250)
    dashboard.mainloop()

#create admin

#main function is running
base=Tk()
base.title("login page")
base.geometry('500x500')

Heading=Label(base,text="Wel come to school",fg="red",font=h1)
Heading.pack()
login=Label(base,text="User Name")
login.pack()
logininput=Entry(base)
logininput.pack()

password=Label(base,text="Password")
password.pack()
passwordinput=Entry(base)
passwordinput.pack()

loginbtn=Button(base,text="Login",command=login_function,bg='blue')
loginbtn.place(y=130,x=220)
signbtn=Button(base,text="create admin")
signbtn.place(y=180,x=200)


exit=Button(base,text="exit", bg="red",command=base.destroy)
exit.place(y=10,x=450)
base.mainloop()