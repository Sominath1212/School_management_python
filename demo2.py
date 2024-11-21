# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("900x500")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("Id", "Name", "DOB","Gender","Email","MO NO","ADDRESS"), show='headings')
tree.column("# 1", anchor=CENTER,width=100)
tree.heading("# 1", text="Id")
tree.column("# 2", anchor=CENTER,width=100)
tree.heading("# 2", text="Name")
tree.column("# 3", anchor=CENTER,width=100)
tree.heading("# 3", text="DOB")
tree.column("# 4", anchor=CENTER,width=100)
tree.heading("# 4", text="Gender")
tree.column("# 5", anchor=CENTER,width=100)
tree.heading("# 5", text="Email")
tree.column("# 6", anchor=CENTER,width=100)
tree.heading("# 6", text="MONO")
tree.column("# 7", anchor=CENTER,width=100)
tree.heading("# 7", text="ADDRESS")



# Insert the data in Treeview widget
tree.insert('', 'end', text="1", values=('299jsjkbds','sominath', '12.12.2002', 'male',"somi@gmail.com","5498594893","N4 cidco"))


tree.pack()

win.mainloop()