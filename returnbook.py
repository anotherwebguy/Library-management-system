from tkinter import messagebox
from tkinter import ttk 
root= Tk()

def disp():
    messagebox.showinfo("ADD","Are you sure you want to submit?")
    
filename = PhotoImage(file ="C:\\Users\\Shashu\\Desktop\\liba3.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame= Frame(root, bg="sky blue")
frame.place(x=150, y=200)
L=Label(frame, text="     RETURN BOOK   ",bg="blue",fg="sky blue",font="Times 20 bold").grid(row=0, column=0)
l1=Label(frame, text="ID NUMBER", bg="black", font="Arial 15", padx=20, fg="yellow").grid(row=10, column=0,pady=10)
input_text=StringVar()
e1=Entry(frame, textvariable=input_text, justify="center").grid(row=10, column=1)
l2=Label(frame, text="BOOK NAME", bg="black", font="Arial 15", padx=20, fg="yellow").grid(row=50, column=0,pady=40)
input1=StringVar()
e2=Entry(frame, textvariable=input1, justify="center").grid(row=50, column=1)
l3=Label(frame, text="DUE DATE", bg="black", font="Arial 15", padx=20, fg="yellow").grid(row=110, column=0)
input2=StringVar()
e3=Entry(frame, textvariable=input2, justify="center").grid(row=110, column=1)
b=Button(frame, text="Submit", font="Arial 15", activeforeground="blue", command=disp).grid(row=200, column=1,pady=25)
root.mainloop()
