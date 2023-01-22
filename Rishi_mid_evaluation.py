from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("TextBox")
menu_=Menu(root)
root.config(menu=menu_)


def fun():
    text_.delete(1.0,END)

def fun1():
    Label_.config(text=text_.get(1.0,END))

def fun2():
    text_file=filedialog.askopenfilename(initialdir="C:/Users/rishi/Onedrive/Documents/Programming/",title="open",filetypes=(("Text Files","*.txt"),))
    text_file=open(text_file,'r')
    stuff=text_file.read()
    text_.insert(END, stuff)
    text_file.close()

def fun3():
    text_file=filedialog.askopenfilename(initialdir="C:/Users/rishi/Onedrive/Documents/Programming/",title="open",filetypes=(("Text Files","*.txt"),))
    text_file=open(text_file,'w')
    text_file.write(text_.get(1.0,END))

def fun4():
    bold_=font.Font(text_,text_.cget("font"))
    bold_.configure(weight="bold")

    text_.tag_configure("bold",font=bold_)

    current_tags = text_.tag_names("sel.first")

    if "bold" in current_tags:
        text_.tag_remove("bold","sel.first","sel.last")
    else:
        text_.tag_add("bold","sel.first","sel.last") 

def fun5():
    italic_=font.Font(text_,text_.cget("font"))
    italic_.configure(slant="italic")

    text_.tag_configure("italic",font=italic_)

    current_tags = text_.tag_names("sel.first")

    if "italic" in current_tags:
        text_.tag_remove("italic","sel.first","sel.last")
    else:
        text_.tag_add("italic","sel.first","sel.last")   


file_=Menu(menu_)
menu_.add_cascade(label="File",menu=file_)
file_.add_command(label="Open",command=fun2)
file_.add_command(label="Save",command=fun3)
file_.add_separator()
file_.add_command(label="Exit",command=root.quit)

edit_=Menu(menu_)
menu_.add_cascade(label="Edit",menu=edit_)
edit_.add_command(label="Copy",command=fun1)
edit_.add_command(label="Clear",command=fun)

font_=Menu(menu_)
menu_.add_cascade(label="Font",menu=font_)
font_.add_command(label="Bold",command=fun4)
font_.add_command(label="Italic",command=fun5)


text_=Text(root,width=200,height=30)
text_.pack()



Label_=Label(root)
Label_.pack()
root.mainloop()