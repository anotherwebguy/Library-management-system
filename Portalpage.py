from tkinter import* 
from tkinter import messagebox
root=Tk()

#----------Inserting Background Image---------------
filename = PhotoImage(file ="C:\\Users\\Shashu\\Desktop\\main.png")
background_label1 = Label(root, image=filename)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

#----------Inserting Images In The Form Of Icons------------ 
filename2 = PhotoImage(file ="C:\\Users\\Shashu\\Desktop\\sp.png")
filename3=PhotoImage(file="C:\\Users\\Shashu\\Desktop\\clg.png")
labelc=Label(root,image=filename3,bd=0)
labelc.place(x=0,y=0)

#----------creating heading label------------
label1=Label(root,text="LIBRARY MANAGEMENT SYSTEM",font=("algerian",30),bg="black",fg="yellow",bd=5,relief=GROOVE)
label8=Label(root,text=" WELCOME TO VIDYAVARDHINI'S COLLEGE LIBRARY",font=("times new roman",27,"italic"),bg="sky blue",fg="red",bd=5,relief=GROOVE)
frame1=Frame(root,bg="white",relief=GROOVE)
frame1.place(x=70,y=200)

#----------creating labels inside frame---------
labeli=Label(frame1,image=filename2,bd=0)
labeli.grid()
label9=Label(root,text="*only for college use",bg="black",fg="white")
label9.place(x=1000,y=580)
label3=Button(root,text="ADD BOOK",font=("times new roman",13,"bold"),bg="white",fg="black",bd=5,relief=GROOVE)
label6=Button(frame1,text="ISSUE BOOK",font=("times new roman",13,"bold"),fg="black",bg="yellow",bd=5,relief=GROOVE)
label7=Button(frame1,text="RETURN BOOK",font=("times new roman",13,"bold"),fg="black",bg="yellow",bd=5,relief=GROOVE)
label10=Button(frame1,text="CHECK AVALIABLE BOOKS",font=("times new roman",13,"bold"),fg="black",bg="yellow",bd=5,relief=GROOVE)
label10.grid(row=6,column=0,pady=30)
label1.grid(row=0,column=0,padx=390)
label8.grid(row=1,column=0,padx=70,pady=10)
label3.place(x=1000,y=600)
label6.grid(row=4,column=0,pady=30)
label7.grid(row=5,column=0,pady=5)
root.mainloop()
