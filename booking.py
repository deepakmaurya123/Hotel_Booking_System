from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector



class Book_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Booking Details")
        self.root.geometry("1281x710+245+79")



        # ===================== variables ==================
        self.var_ref=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_nodays=StringVar()


        # title label ##################################
        t_lbl=Label(self.root,text="Room Booking",font=("times new roman",24,"bold"),bg="black",fg="yellow")
        t_lbl.place(x=0,y=0,width=1280,height=38)


        # left label frame ######################################################################
        Left_label_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="Customer Details",font=("times new roman",15,"bold"),pady=10) 
        Left_label_frame.place(x=10,y=38,width=400,height=490)


        # customer ref
        cust_ref=Label(Left_label_frame,text="Customer Ref",font=("times new roman",14,"bold"),pady=10)
        cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(Left_label_frame,width=13,textvariable=self.var_ref,font=("times new roman",14,"bold"))
        entry_ref.grid(row=0,column=1,padx=10,sticky=W)

        # fetch button side of ref
        fetch=Button(Left_label_frame,command=self.fetch_ref,text="Fetch Data",cursor="hand2",font=("times new roman",13,"bold"),bg="black",fg="yellow",width=9)
        fetch.place(x=290,y=7)


        # check-in date
        check_out=Label(Left_label_frame,text="Check-in Date",font=("times new roman",14,"bold"),pady=10)
        check_out.grid(row=1,column=0,sticky=W)

        entry_checkout=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_checkin,font=("times new roman",14,"bold"))
        entry_checkout.grid(row=1,column=1,padx=10)


        # check out date
        room_no=Label(Left_label_frame,text="Check-out Date",font=("times new roman",14,"bold"),pady=10)
        room_no.grid(row=2,column=0,sticky=W)

        entry_roomno=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_checkout,font=("times new roman",14,"bold"))
        entry_roomno.grid(row=2,column=1,padx=10)

        
        # floor
        check_in=Label(Left_label_frame,text="Floor",font=("times new roman",14,"bold"),pady=10)
        check_in.grid(row=3,column=0,sticky=W)

        floor=ttk.Combobox(Left_label_frame,textvariable=self.var_floor,font=("times new roman",13,"bold"),state="readonly",width=20)
        floor["values"]=("Select Floor","Ground","First","Second","Third","Fourth")
        floor.current(0)
        floor.grid(row=3,column=1,padx=10)


        # room number
        no_days=Label(Left_label_frame,text="Room Number",font=("times new roman",14,"bold"),pady=10)
        no_days.grid(row=4,column=0,sticky=W)

        entry_nodays=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_roomno,font=("times new roman",14,"bold"))
        entry_nodays.grid(row=4,column=1,padx=10)


        # no of days
        no_days=Label(Left_label_frame,text="No of Days",font=("times new roman",14,"bold"),pady=10)
        no_days.grid(row=5,column=0,sticky=W)

        entry_nodays=ttk.Entry(Left_label_frame,width=20,textvariable=self.var_nodays,font=("times new roman",14,"bold"))
        entry_nodays.grid(row=5,column=1,padx=10)


        # button frame ##################################################
        btn_frame=Frame(Left_label_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=395,height=40)

        # add button
        add=Button(btn_frame,text="Add",cursor="hand2",command=self.add_data,font=("times new roman",14,"bold"),bg="black",fg="yellow",width=7)
        add.grid(row=0,column=0,padx=4)

        # update button
        update=Button(btn_frame,text="Update",cursor="hand2",command=self.update,font=("times new roman",14,"bold"),bg="black",fg="yellow",width=7)
        update.grid(row=0,column=1,padx=6)

        # delete button
        delete=Button(btn_frame,text="Delete",cursor="hand2",command=self.delete,font=("times new roman",14,"bold"),bg="black",fg="yellow",width=7)
        delete.grid(row=0,column=2,padx=6)


        # reset button
        reset=Button(btn_frame,text="Reset",cursor="hand2",command=self.reset,font=("times new roman",14,"bold"),bg="black",fg="yellow",width=7)
        reset.grid(row=0,column=3,padx=6)



        # =========================  RIGHT SIDE FETCH DATA ============================
        





        ## right frame ################################################
        right_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="View Booking Details",font=("times new roman",15,"bold"),pady=1)
        right_frame.place(x=420,y=240,width=850,height=450)


        ###  table frame ##############################
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=5,width=820,height=400)


        #  show table ##########################################
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(table_frame,columns=("ref","checkin","checkout","floor","roomno","nodays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)                    
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)


        self.cust_details_table.heading("ref",text="Refer No")
        self.cust_details_table.heading("checkin",text="Check-in Date")
        self.cust_details_table.heading("checkout",text="Check-out Date")
        self.cust_details_table.heading("floor",text="Floor")
        self.cust_details_table.heading("roomno",text="Room Number")
        self.cust_details_table.heading("nodays",text="No of Days")


        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("checkin",width=100)
        self.cust_details_table.column("checkout",width=100)
        self.cust_details_table.column("floor",width=100)
        self.cust_details_table.column("roomno",width=100)
        self.cust_details_table.column("nodays",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def fetch_ref(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Error","Please enter ref number",parent=self.root) 
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
            my_cursor=conn.cursor() 
            query=("select Name from customer where Ref_No=%s") 
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Customer not found",parent=self.root)
            else:
                conn.commit()
                conn.close() 

                # fetch frame ######################################################################
                fetch_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="Fetched Data",font=("times new roman",14,"bold"),pady=10)  
                fetch_frame.place(x=420,y=38,width=300,height=200)

                # name label
                name_label=Label(fetch_frame,text="Name:",font=("times new roman",14,"bold"),padx=10)  
                name_label.grid(row=0,column=0,sticky=W) 

                name_value=Label(fetch_frame,text=row[0],font=("times new roman",14,"bold"))  
                name_value.grid(row=0,column=1,padx=10,sticky=W)

                # gender label
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
                my_cursor=conn.cursor() 
                query=("select Gender from customer where Ref_No=%s") 
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                conn.close()

                gender_label=Label(fetch_frame,text="Gender:",font=("times new roman",14,"bold"),padx=10)  
                gender_label.grid(row=1,column=0,sticky=W) 

                gender_value=Label(fetch_frame,text=row,font=("times new roman",14,"bold"))  
                gender_value.grid(row=1,column=1,padx=10,sticky=W)


                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
                my_cursor=conn.cursor() 
                query=("select Mobile from customer where Ref_No=%s") 
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                conn.close()

                mobile_label=Label(fetch_frame,text="Mobile:",font=("times new roman",14,"bold"),padx=10)  
                mobile_label.grid(row=2,column=0,sticky=W) 

                mobile_value=Label(fetch_frame,text=row,font=("times new roman",14,"bold"))  
                mobile_value.grid(row=2,column=1,padx=10,sticky=W)

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
                my_cursor=conn.cursor() 
                query=("select City from customer where Ref_No=%s") 
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                conn.close()

                city_label=Label(fetch_frame,text="City:",font=("times new roman",14,"bold"),padx=10)  
                city_label.grid(row=3,column=0,sticky=W) 

                city_value=Label(fetch_frame,text=row,font=("times new roman",14,"bold"))  
                city_value.grid(row=3,column=1,padx=10,sticky=W)

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
                my_cursor=conn.cursor() 
                query=("select State from customer where Ref_No=%s") 
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                conn.close()

                state_label=Label(fetch_frame,text="State:",font=("times new roman",14,"bold"),padx=10)  
                state_label.grid(row=4,column=0,sticky=W) 

                state_value=Label(fetch_frame,text=row[0],font=("times new roman",14,"bold"))  
                state_value.grid(row=4,column=1,padx=10,sticky=W)




                # =====================  BUTTON FUNCTION ============================
    def add_data(self):
        
        if self.var_roomno.get()=="":
            messagebox.showerror("Error","Some Entries are not filled",parent=self.root)                
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s)",(
                                                                          self.var_ref.get(),
                                                                          self.var_checkin.get(),
                                                                          self.var_checkout.get(),
                                                                          self.var_floor.get(),
                                                                          self.var_roomno.get(),
                                                                          self.var_nodays.get()
                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","room is alloted",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root)  

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)>=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
        conn.commit    
        conn.close() 



    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_floor.set(row[3])        
        self.var_roomno.set(row[4])
        self.var_nodays.set(row[5])                         
                   
                   
    
    def update(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Error","Please enter reference number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in_Date=%s, Check_out_Date=%s, Floor=%s, Room=%s, No_of_Days=%s  where Ref_No=%s",(
                                                                                                                            self.var_checkin.get(),
                                                                                                                            self.var_checkout.get(),
                                                                                                                            self.var_floor.get(),
                                                                                                                            self.var_roomno.get(),
                                                                                                                            self.var_nodays.get(),
                                                                                                                            self.var_ref.get()                                                                                 
                                                                                                                           ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    def delete(self):
        mdelete=messagebox.askyesno("Hotel Booking System","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="booking")
            my_cursor=conn.cursor()
            query="delete from room where Ref_No=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Room details has been deleted successfully",parent=self.root)  


    def reset(self):
        self.var_ref.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        #self.var_floor.set("")        
        self.var_roomno.set("")
        self.var_nodays.set("")










if __name__=="__main__":
    root=Tk()
    obj=Book_window(root)
    root.mainloop()         