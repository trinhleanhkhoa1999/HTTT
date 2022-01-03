import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os



root = Tk()
root.title("Mã hóa AES")
root.configure(background="#eeeeee")




def close_window ():
    if messagebox.askyesno("Question","Bạn muốn thoát ?")==True:
        root.destroy()
    else:
        pass
        
def kill1():
    root.destroy()
    os.system('MaHoa.py')
    
    
def kill2():
    root.destroy()
    os.system('GiaiMa.py')
    
   
def kill3():
    root.destroy()
    os.system('MaHoaFile.py')
 
    
    

labelfont = ('times', 20, 'bold')
widget = Label(root, text='MÃ HÓA AES')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.grid(padx=0,pady=0,ipadx=24,ipady=6,row=1,column=0,rowspan = 4,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)
  
select_btn = tk.Button(root,text="Mã hóa văn bản",command=kill1,width=42,
                       bg="#1089ff",fg="#ffffff",bd=2,relief=tk.FLAT)
select_btn.grid(padx=30,pady=8,ipadx=24,ipady=6,row=5,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)
select_btn2 = tk.Button(root,text="Giải mã văn bản",command=kill2,width=42,
                       bg="#ed3833",fg="#ffffff",bd=2,relief=tk.FLAT)
select_btn2.grid(padx=30,pady=8,ipadx=24,ipady=6,row=6,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)
select_btn3 = tk.Button(root,text="Mã hóa file",command=kill3,width=42,
                       bg="#00bd56",fg="#ffffff",bd=2,relief=tk.FLAT)
select_btn3.grid(padx=30,pady=8,ipadx=24,ipady=6,row=7,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)
select_btn4 = tk.Button(root,text="Thoát",command=close_window,width=42,
                       bg="#aaaaaa",fg="#ffffff",bd=2,relief=tk.FLAT)
select_btn4.grid(padx=30,pady=8,ipadx=24,ipady=6,row=8,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)



tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 1, weight=1)
tk.Grid.columnconfigure(root, 2, weight=1)
tk.Grid.columnconfigure(root, 3, weight=1)





mainloop()
root.mainloop()






