from tkinter import *
from tkinter import messagebox
Right = Tk()

filename = PhotoImage(file ="C:\\Users\\Shashu\\Desktop\\oldbook.png")
background_label = Label(Right, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
filename3=PhotoImage(file="C:\\Users\\Shashu\\Desktop\\vidya.png")
labelc=Label(Right,image=filename3,bd=0)
labelc.place(x=1090,y=0)

def disp():
    messagebox.showinfo("ADD","You have added the book")

clicked = StringVar()
clicked.set("Select")
l = Label(Right, text="Add Books", font=("algerian",40),bg="black",fg="blue")
l.pack()
f1 = Frame(Right).place(x=40, y=100)
l1 = Label(f1, text="Name of the Book", font="Arial 16",fg="blue").place(x=100, y=140)
e = Entry(f1, bd=1).place(x=340, y=140)
l2 = Label(f1, text="Author", font="Arial 16",fg="blue").place(x=100, y=200)
e1 = Entry(f1, bd=1).place(x=340, y=200)
l3 = Label(f1, text="No. of copies", font="Arial 16",fg="blue").place(x=100, y=260)
e2 = Entry(f1, bd=1).place(x=340, y=260)
l4 = Label(f1, text="Category", font="Arial 16",fg="blue").place(x=100, y=325)
drop = OptionMenu(f1, clicked, "Astronomy", "Sci-Fiction", "Novels", "Encyclopedia", "Engineering material", "Competitive Exam Study material", "Business Times", "Reference Books").place(x=370, y=318)
btn = Button(f1,  text="Add", font="Arial 16", activeforeground="blue", command=disp).place(x=260, y=390)
Right.mainloop()

