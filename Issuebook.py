from tkinter import *
from tkinter import messagebox
root = Tk()
def issue_book():
    #====variables===
    title=Label(root,text="Book issue system",font=("times new roman",40,"bold"),bg="powder      blue",fg="black",bd=5,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)
    Book_Frame=Frame(root,bg="white")
    Book_Frame.place(x=300,y=20
    lbluser=Label(Book_Frame,text="Enter Name",bd=0,font=("times new roman",18,"bold"))                  lbluser.grid(row=1,column=0,padx=20,pady=10)
    txtuser=Entry(Book_Frame,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)       
    lblid=Label(Book_Frame,text="Enter your student ID no.",bd=0,font=("times new roman",18,"bold"))
    lblid.grid(row=2,column=0,padx=20,pady=10)
    txtid=Entry(Book_Frame,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20) 
    bookname=StringVar()
    lblbook=Label(Book_Frame,text="Enter book name",bd=0,font=("times new roman",18,"bold")).grid(row=3,column=0,padx=20,pady=10)        txtbook=Entry(Book_Frame,bd=5,textvariable=bookname,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)  btn=Button(Book_Frame,text="Search Book",width=15,command=boona,font=("times new roman",14,"bold"),fg="blue)
    bt1=Button(Book_Frame, text="Exit", width=15, command=Book_Frame.quit, font="times 14 bold", fg="blue") bt1.grid(row=5, column=1, pady=10)               

def boona():
    messagebox.showinfo("Book","Book is Available")

issue_book()
root.mainloop()

