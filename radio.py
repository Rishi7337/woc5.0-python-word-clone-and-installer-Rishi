from tkinter import *
root = Tk()
root.title("radiobutton")

select=Label(root,text="Select your Sport").pack()

sport=StringVar()
sport.set("Cricket")

Sports=[("Cricket","Cricket"),("Football","Football"),("Hockey","Hockey")]
for text,Sport in Sports:
    Radiobutton(root,text=text,variable=sport,value=Sport).pack()

def fun(value):
    lable=Label(root,text=value)
    lable.pack()

b=Button(root,text="you selected",command=lambda:fun(sport.get())).pack()

root.mainloop()