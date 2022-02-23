from tkinter import *
#from PIL import ImageTk,Image


# main window
root = Tk()
root.title("FrEe FiRe.exe")
#root.geometry("480x380")
root.configure(bg="#ffffff")

frame0 = LabelFrame(root, text="frames")
frame0.pack(side=TOP, fill=BOTH, expand=TRUE)

#Frames
frame1 = LabelFrame(frame0,
 text="EMU's",
 padx=1,
 pady=1,
 height=240,
 width=160)
#frame1.grid(row=0 ,column=0 ,padx=1, pady=1)
frame1.pack(side=LEFT, fill=BOTH, expand=TRUE)
frame2 = LabelFrame(frame0,
 text="EMU's",
 padx=1,
 pady=1,
 height=240,
 width=160)
#frame2.grid(row=0 ,column=2 ,padx=1, pady=1)
frame2.pack(side=LEFT, fill=BOTH, expand=TRUE)
frame3 = Frame(root,
 padx=1,
 pady=1,
 bg="#000000")
#frame3.grid(row=1, padx=1, pady=1)
frame3.pack(fill=BOTH, expand=TRUE)
#buttons
mybutton = Button(frame2,
 text='Regedit',
 width=10,
 height=2,
 bg='#ffffff',
 fg='#000000',
 activebackground='#ffe992',
 activeforeground='#000000')
mybutton.grid(row=0 ,column=0 ,padx=1, pady=1)

btn2 = Button(frame2,
 text='20%_Headshot',
 width=10,
 height=2,
 bg='#ffffff',
 fg='#000000',
 activebackground='#ffe992', 
 activeforeground='#000000')
btn2.grid(row=0 ,column=1 ,padx=1, pady=1)

btn3 = Button(frame2,
 text='50%_Headshot',
 width=10,
 height=2,
 bg='#ffffff',
 fg='#000000',
 activebackground='#ffe992', 
 activeforeground='#000000')
btn3.grid(row=1 ,column=0 ,padx=1, pady=1)

btn4 = Button(frame2,
 text='Auto_AimLock()',
 width=10,
 height=2,
 bg='#ffffff',
 fg='#000000',
 activebackground='#ffe992', 
 activeforeground='#000000')
btn4.grid(row=1 ,column=1 ,padx=1, pady=1)

#frame1 radio buttons

r = IntVar()


Radiobutton(frame1, text="Bluestackes", variable=r, value=1).pack(anchor=W)
Radiobutton(frame1, text="NoxPlayer", variable=r, value=2).pack(anchor=W)
Radiobutton(frame1, text="SmartGaga", variable=r, value=3).pack(anchor=W)
Radiobutton(frame1, text="LD Player", variable=r, value=4).pack(anchor=W)

# frame3
setbs = Label(frame3, text="..Emulator set to bluestackes", bg="#000000", fg="#00ff00")
setbs.pack()



root.mainloop()
