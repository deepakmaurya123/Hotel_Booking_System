from tkinter import *
from tkinter import ttk
from numpy import random
import mysql.connector
from tkinter import messagebox

class Cust_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Customers")
        self.root.geometry("1281x710+245+79")


        # =========================   variables ================================================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_city=StringVar()
        self.var_state=StringVar()


        # title label
        t_lbl=Label(self.root,text="Add Customer Details",font=("times new roman",24,"bold"),bg="black",fg="yellow")
        t_lbl.place(x=0,y=0,width=1280,height=38)  


        
        
        # left label frame ##############################################################################
        Left_label_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="Customer Details",font=("times new roman",15,"bold"),pady=10) 
        Left_label_frame.place(x=10,y=38,width=400,height=650)  


        # customer ref
        cust_ref=Label(Left_label_frame,text="Customer Ref",font=("times new roman",14,"bold"),pady=20)
        cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_ref,font=("times new roman",14,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1,padx=10)

        
        # customer name
        cust_name=Label(Left_label_frame,text="Customer Name",font=("times new roman",14,"bold"),pady=20)
        cust_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_cust_name,font=("times new roman",14,"bold"))
        entry_name.grid(row=1,column=1,padx=10)


        # gender
        gender=Label(Left_label_frame,text="Gender",font=("times new roman",14,"bold"),pady=20)
        gender.grid(row=2,column=0,sticky=W)

        gender_combo=ttk.Combobox(Left_label_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1)


        # mobile
        mobile=Label(Left_label_frame,text="Mobile",font=("times new roman",14,"bold"),pady=20)
        mobile.grid(row=3,column=0,sticky=W)

        entry_mobile=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_mobile,font=("times new roman",14,"bold"))
        entry_mobile.grid(row=3,column=1,padx=10)


        # id proof type
        id_proof=Label(Left_label_frame,text="Id Proof Type",font=("times new roman",14,"bold"),pady=20)
        id_proof.grid(row=4,column=0,sticky=W)

        id_proof_combo=ttk.Combobox(Left_label_frame,textvariable=self.var_id_proof,font=("times new roman",13,"bold"),state="readonly",width=20)
        id_proof_combo["values"]=("Select ID Proof type","Adhar Card","Driving License","Passport","Voter ID")
        id_proof_combo.current(0)
        id_proof_combo.grid(row=4,column=1)


        # id number
        id_number=Label(Left_label_frame,text="Id Number",font=("times new roman",14,"bold"),pady=20)
        id_number.grid(row=5,column=0,sticky=W)

        entry_id=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_id_number,font=("times new roman",14,"bold"))
        entry_id.grid(row=5,column=1,padx=10)


         # city
        city=Label(Left_label_frame,text="City",font=("times new roman",14,"bold"),pady=20)
        city.grid(row=6,column=0,sticky=W)

        entry_city=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_city,font=("times new roman",14,"bold"))
        entry_city.grid(row=6,column=1,padx=10,sticky=W)
        
        # state
        state=Label(Left_label_frame,text="State",font=("times new roman",14,"bold"),pady=20)
        state.grid(row=7,column=0,sticky=W)

        entry_country=ttk.Entry(Left_label_frame,textvariable=self.var_state,width=20,font=("times new roman",14,"bold"))
        entry_country.grid(row=7,column=1,padx=10)






        # button frame ##################################################
        btn_frame=Frame(Left_label_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=550,width=395,height=40)


        # add button
        add=Button(btn_frame,text="Add",cursor="hand2",command=self.add_data,font=("times new roman",14,"bold"),bg="black",fg="white",width=7)
        add.grid(row=0,column=0,padx=6)
  

        # update button
        update=Button(btn_frame,text="Update",cursor="hand2",command=self.update,font=("times new roman",14,"bold"),bg="black",fg="white",width=7)
        update.grid(row=0,column=1,padx=5)


        # delete button
        delete=Button(btn_frame,text="Delete",cursor="hand2",command=self.delete,font=("times new roman",14,"bold"),bg="black",fg="white",width=7)
        delete.grid(row=0,column=2,padx=5)


        # reset button
        delete=Button(btn_frame,text="Reset",cursor="hand2",command=self.reset,font=("times new roman",14,"bold"),bg="black",fg="white",width=7)
        delete.grid(row=0,column=3,padx=5)


        # right label frame ################################################
        right_label_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="View Customer Details",font=("times new roman",15,"bold"),pady=10) 
        right_label_frame.place(x=420,y=38,width=850,height=650)






        ## table frame ################################################
        table_frame=Frame(right_label_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=15,width=830,height=580)

        #  show table ##########################################
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(table_frame,columns=("ref","name","gender","mobile","id_proof","id_no","city","state"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)                    
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)


        self.cust_details_table.heading("ref",text="Refer No")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("mobile",text="Mobile")
        self.cust_details_table.heading("id_proof",text="Id Proof")
        self.cust_details_table.heading("id_no",text="Id number")
        self.cust_details_table.heading("city",text="City")
        self.cust_details_table.heading("state",text="State")


        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=150)
        self.cust_details_table.column("gender",width=80)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("id_proof",width=100)
        self.cust_details_table.column("id_no",width=100)
        self.cust_details_table.column("city",width=100)
        self.cust_details_table.column("state",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    # ======================== BUTTON FUNCTIONS =================================================
    
    def add_data(self):
        
        if self.var_cust_name.get()=="" or self.var_mobile.get()=="" or self.var_id_number.get()=="" or self.var_city.get()=="" or self.var_state.get()=="":
            messagebox.showerror("Error","Some Entries are not filled",parent=self.root)            
        elif self.var_gender.get()=="Select Gender":
            messagebox.showerror("Error","Gender not selected",parent=self.root)
        elif self.var_id_proof.get()=="Select ID Proof type":
            messagebox.showerror("Error","Id proof not selected",parent=self.root)    
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                          self.var_ref.get(),
                                                                          self.var_cust_name.get(),
                                                                          self.var_gender.get(),
                                                                          self.var_mobile.get(),
                                                                          self.var_id_proof.get(),
                                                                          self.var_id_number.get(),
                                                                          self.var_city.get(),
                                                                          self.var_state.get()
                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root)                                                              

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)>=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit    
            conn.close()    

    
    
    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_mobile.set(row[3])
        self.var_id_proof.set(row[4])
        self.var_id_number.set(row[5])
        self.var_city.set(row[6])
        self.var_state.set(row[7])
  


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s, Gender=%s, Mobile=%s, ID_Proof=%s, Id_Number=%s, City=%s, State=%s where Ref_No=%s",(
                                                                                                                            self.var_cust_name.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_mobile.get(),
                                                                                                                            self.var_id_proof.get(),
                                                                                                                            self.var_id_number.get(),
                                                                                                                            self.var_city.get(),
                                                                                                                            self.var_state.get(),
                                                                                                                            self.var_ref.get()                                                                                 
                                                                                                                                                    
                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def delete(self):
        mdelete=messagebox.askyesno("Hotel Booking System","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
            my_cursor=conn.cursor()
            query="delete from customer where Ref_No=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Customer details has been deleted successfully",parent=self.root)       



    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set("")
        #self.var_gender.set("")
        self.var_mobile.set("")
        #self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_city.set("")
        self.var_state.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))



            


        










if __name__=="__main__":
    root=Tk()
    obj=Cust_window(root)
    root.mainloop()          
