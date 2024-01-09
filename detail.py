from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector



class detail_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Project Developer")
        self.root.geometry("1281x710+245+79")

        # title label
        title_lbl=Label(self.root,text="Project Developer Details",font=("times new roman",28,"bold"),bg="red",fg="lime")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        frame=Frame(self.root,bd=4,relief=RIDGE) 
        frame.place(x=10,y=50,width=1266,height=655)

        # text insert
        T = Text(frame,font=("times new roman",30,"bold",),bg="black",fg="white")
        T.place(x=0,y=0,width=1266,height=655)
        
        
        quote = """Project Developer:\n\n
Name: Deepak Kumar Maurya
Course - MCA (2021 - 2023)

Technology Used - Python, Tkinter, MySQL



Thank You!!!"""
        
        
        T.insert(INSERT, quote)
        T.config(state=DISABLED)


if __name__=="__main__":
    root=Tk()
    obj=detail_window(root)
    root.mainloop()         