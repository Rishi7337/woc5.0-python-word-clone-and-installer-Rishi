from tkinter import *

root=Tk()
root.title("Frames")


frame=LabelFrame(root,text="Here is a Frame",padx=10,pady=10)
frame.pack(padx=30,pady=30)
e=Entry(frame,width=20)
e.grid(row=0,column=2)
def fun():
    e.delete(0,END)
    s="Dont Click"
    e.insert(0,s)
b=Button(frame,text="Dont click",command=fun)
b.grid(row=0,column=1)
root.mainloop()