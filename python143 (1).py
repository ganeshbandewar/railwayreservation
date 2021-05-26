from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def book():
    a=e_a.get()
    b=e_b.get();
    c=e_c.get();
    d=e_d.get();

    if(a=="" or b=="" or c=="" or d==''):
      MessageBox.showinfo("book staus", "all fielsds required ")
    else:
     con= mysql.connect(host="localhost" ,user="root" ,password="fyty@4521", database="railway1")
     cursor = con.cursor()
     cursor.execute("insert into rail values('"+ a +"', '"+ b +"', '"+ c +"', '"+ d +"')")
     cursor.execute("commit");
     MessageBox.showinfo("book status", "booked succesfully");
     con.close();
 
def cancel():
    if(e_a.get() == ""):
        MessageBox.showinfo("cancel status", "a is compulsory for deleting")
    else:
     con= mysql.connect(host="localhost" ,user="root" ,password="fyty@4521", database="railway1")
     cursor = con.cursor()
     cursor.execute("delete from rail where a='"+ e_a.get() +"'")
     cursor.execute("commit");
     MessageBox.showinfo("cancel status", "cancelled succesfully");
     con.close();

def seat():
    con= mysql.connect(host="localhost" ,user="root" ,password="fyty@4521", database="railway1")
    cursor = con.cursor()
    cursor.execute("select * from rail")
    rows=cursor.fetchall()

    for row in rows:
        insertdata= str(row[0])+' ' +str(row[1])+' '+ row[2]+' '+ row[3]
        list.insert(list.size()+3, insertdata)
    con.close()
root = Tk()
root.geometry("600x400")
root.title("Python + Database")

s=Label(root, text = "Railway Reservation Management System",  background = 'blue', foreground ="white",  
font = ("Times New Roman", 15))
s.place(x = 150, y = 10) 
a=Label(root, text='Enter Train No', font=('bold', 10))
a.place(x=20,y=60);
b=Label(root, text='Journey Date', font=('bold', 10))
b.place(x=20,y=90);
c=Label(root, text='Source Station', font=('bold', 10))
c.place(x=20,y=120);
d=Label(root, text='Destination Station', font=('bold', 10))
d.place(x=20,y=150);

e_a = Entry()
e_a.place(x=150,y=60)

e_b = Entry()
e_b.place(x=150,y=90)

e_c = Entry()
e_c.place(x=150,y=120)

e_d = Entry()
e_d.place(x=150,y=150)

book = Button(root, text="Book Ticket", font=("bold",10),bg="white", command=book)
book.place(x=20,y=190)

cancel = Button(root, text="Cancel Ticket", font=("bold",10),bg="white", command=cancel)
cancel.place(x=120,y=190)

seat = Button(root, text="Seat Status", font=("bold",10),bg="white", command=seat)
seat.place(x=220,y=190)

list= Listbox(root)
list.place(x=350, y=60)



root.mainloop()
