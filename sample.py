from tkinter import *

# main window
root = Tk()
root.title("FrEe FiRe.exe")
root.geometry("480x380")
root.configure(bg="#ffffff")


mybutton = Button(root,
 text='My Button',
 width=10,
 height=2,
 bg='#ffffff',
 fg='#000000',
 activebackground='#ffe992',
 activeforeground='#000000')
mybutton.pack()

btn2 = Button(root,
 text='My Button',
 width=10,
 height=2,
 bg='#ffffff',
 fg='#000000',
 activebackground='#ffe992', 
 activeforeground='#000000')
btn2.pack()


btn3 = Button(root,
 text='My Button',
 width=10,
 height=2,
 bg='#ffffff',
 fg='#000000',
 activebackground='#ffe992', 
 activeforeground='#000000')
btn3.pack()

btn4 = Button(root,
 text='My Button',
 width=10,
 height=2,
 bg='#ffffff',
 fg='#000000',
 activebackground='#ffe992', 
 activeforeground='#000000')
btn4.pack()

root.mainloop()
