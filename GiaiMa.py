import tkinter as tk
from tkinter import *
from Crypto.Cipher import AES
import sys
import base64
import codecs
import os
import hashlib
from tkinter import messagebox

root = Tk()
root.title("Giải mã văn bản")
root.configure(bg="#eeeeee")

    
label1 = tk.Label(root,text="Nhập key tại đây: ",bg="#eeeeee",anchor=tk.W)
label1.grid(padx=12,pady=(8, 0),ipadx=0,ipady=1,row=0,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)

ent = tk.Entry(root,bg="#fff",exportselection=0,relief=tk.FLAT)

ent.grid(padx=15,pady=6,ipadx=8,ipady=8,row=1,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)


label2 = tk.Label(root,text="Nhập văn bản mã hóa tại đây: ",bg="#eeeeee",anchor=tk.W)
label2.grid(padx=12,pady=(8, 0),ipadx=0,ipady=1,row=3,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)

text2 = tk.Text(root,bg="#fff",relief=tk.FLAT)
text2.grid(padx=15,pady=6,ipadx=8,ipady=8,row=4,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)


label2 = tk.Label(root,text="Văn bản giải mã: ",bg="#eeeeee",anchor=tk.W)
label2.grid(padx=12,pady=(8, 0),ipadx=0,ipady=1,row=7,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)

text3 = tk.Text(root,bg="#fff",relief=tk.FLAT)
text3.grid(padx=15,pady=6,ipadx=8,ipady=8,row=8,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)
text3.insert('1.0', "")

def pad(text1):
    while len(text1)% 16 != 0:
        text1 = text1 + " "
    return text1

def fetch():
    try:
        text1 = text2.get('1.0',END)
        text100 = text1.strip()
        text200 = text100.encode()
        msg = base64.b64decode(text200)
        print(msg)
        abc= ent.get()
        password = abc.encode()
        key = hashlib.sha256(password).digest()
        mode = AES.MODE_CBC
        IV = 'This is an IV456'
        cipher = AES.new(key, mode, IV.encode("utf8"))
        decrypted = cipher.decrypt(msg)
        text3.delete(1.0, END)
        print(decrypted.rstrip().decode())
    except:
        print('Có lỗi khi giải mã')
    
class StdoutRedirector(object):

    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.insert(END, str)
        self.text_area.see(END)
sys.stdout = StdoutRedirector(text3)        
   
select_btn = tk.Button(root,text="Giải mã",command=fetch,width=42,
                       bg="#1089ff",fg="#ffffff",bd=2,relief=tk.FLAT)
select_btn.grid(padx=15,pady=8,ipadx=24,ipady=6,row=5,column=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)

def refesh():
    text2.delete('1.0',END)
    text3.delete('1.0',END)
    ent.delete(0,END)
def close_window ():
    if messagebox.askyesno("Question","Bạn muốn quay lại ?")==True:
        root.destroy() 
        os.system('Menu.py')     
    else:
        pass          
refresh_btn = tk.Button(
            root,
            text="Làm mới",
            command=refesh,
            bg="#aaaaaa",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
refresh_btn.grid(
            padx=(15, 6),
            pady=8,
            ipadx=24,
            ipady=6,
            row=6,
            column=0,
            columnspan=2,
            sticky=tk.W+tk.E+tk.N+tk.S
        )
        
back_btn = tk.Button(
            root,
            text="Quay lại",
            command=close_window,
            bg="#aaaaaa",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
back_btn.grid(
            padx=(6, 15),
            pady=8,
            ipadx=24,
            ipady=6,
            row=6,
            column=2,
            columnspan=2,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 1, weight=1)
tk.Grid.columnconfigure(root, 2, weight=1)
tk.Grid.columnconfigure(root, 3, weight=1)





mainloop()
root.mainloop()

