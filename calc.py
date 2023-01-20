from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_num(number):

    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_cl():
    e.delete(0,END)

def button_equal():
    sec_num=int(e.get())
    e.delete(0,END)
    
    if op =="addition":
        e.insert(0,sec_num+f_num)

    if op=="subtraction":
        e.insert(0,f_num-sec_num)

    if op=="multiplication":
        e.insert(0,sec_num*f_num)

    if op=="division":
        e.insert(0,f_num/sec_num)



def button_add():
    first_number=e.get()
    global f_num
    global op
    op="addition"
    f_num=int(first_number)
    
    e.delete(0,END)


def button_sub():
    first_number=e.get()
    global f_num
    global op
    op="subtraction"
    f_num=int(first_number)
    
    e.delete(0,END)
    return

def button_mul():
    first_number=e.get()
    global f_num
    global op
    op="multiplication"
    f_num=int(first_number)
    
    e.delete(0,END)
    return    

def button_div():
    first_number=e.get()
    global f_num
    global op
    op="division"
    f_num=int(first_number)
    
    e.delete(0,END)
    return


     
butt1=Button(root,text="1",padx=40,pady=20,command=lambda: button_num(1))
butt2=Button(root,text="2",padx=40,pady=20,command=lambda: button_num(2))
butt3=Button(root,text="3",padx=40,pady=20,command=lambda: button_num(3))
butt4=Button(root,text="4",padx=40,pady=20,command=lambda: button_num(4))
butt5=Button(root,text="5",padx=40,pady=20,command=lambda: button_num(5))
butt6=Button(root,text="6",padx=40,pady=20,command=lambda: button_num(6))
butt7=Button(root,text="7",padx=40,pady=20,command=lambda: button_num(7))
butt8=Button(root,text="8",padx=40,pady=20,command=lambda: button_num(8))
butt9=Button(root,text="9",padx=40,pady=20,command=lambda: button_num(9))
butt0=Button(root,text="0",padx=40,pady=20,command=lambda: button_num(0))
buttadd=Button(root,text="+",padx=39,pady=20,command=lambda: button_add())
buttcl=Button(root,text="Clear",padx=79,pady=20,command=lambda: button_cl())
butteq=Button(root,text="=",padx=89,pady=20,command=lambda: button_equal())
buttsub=Button(root,text="-",padx=40,pady=20,command=lambda: button_sub())
buttmul=Button(root,text="*",padx=40,pady=20,command=lambda: button_mul())
buttdiv=Button(root,text="/",padx=41,pady=20,command=lambda: button_div())


butt1.grid(row=3 ,column =0)
butt2.grid(row=3 ,column =1)
butt3.grid(row=3 ,column =2)

butt4.grid(row=2 ,column =0)
butt5.grid(row=2 ,column =1)
butt6.grid(row=2 ,column =2)

butt7.grid(row=1 ,column =0)
butt8.grid(row=1 ,column =1)
butt9.grid(row=1 ,column =2)

butt0.grid(row=4 ,column =0)
buttadd.grid(row=5,column=0)
buttcl.grid(row=4,column=1,columnspan=2)
butteq.grid(row=5,column=1,columnspan=2)
buttsub.grid(row=6,column=0)
buttmul.grid(row=6,column=1)
buttdiv.grid(row=6,column=2)

root.mainloop()
