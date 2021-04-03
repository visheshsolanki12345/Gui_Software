from tkinter import*
from tkinter import messagebox, ttk
import pymysql

class SchoolSystem():
    def __init__(self,root):
        self.root = root
        self.root.title("School Managment | Developer By VISHESH")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root,text="Student Managment System", font=("times new roman",25,"bold"),bg="blue",fg="white",padx=10).place(x=0,y=0, relwidth=1)

        
        ################## Frame 1 ###########################

        ################## Variable #########################
        self.var_stu_roll = StringVar()
        self.var_stu_Name = StringVar()
        self.var_stu_f_name = StringVar()
        self.var_stu_m_name = StringVar()
        self.var_stu_email = StringVar()
        self.var_stu_gender = StringVar()
        self.var_stu_contact = StringVar()
        self.var_stu_dob = StringVar()

        self.var_stu_search_by = StringVar()
        self.var_stu_search_txt = StringVar()
        #self.var_stu_address = StringVar()


        frame1 = Frame(self.root,bd=10,relief=RIDGE,bg='red')
        frame1.place(x=10,y=50,width=450,height=640)

        ################ Lable or Entry ######################
        title1 = Label(frame1,text='Manage Students',font=('times new roman',25,'bold'),fg='white',bg='red')
        title1.place(x=80,y=10)

        lbl_roll = Label(frame1,text="Roll No.", font=("times new roman",20),bg="red",fg="white").place(x=10,y=60)
        ent_roll = Entry(frame1, font=("times new roman",15),textvariable=self.var_stu_roll,bg="white",fg="black")
        ent_roll.place(x=200,y=60,width=200,height=30)
        
        lbl_Name = Label(frame1,text="Student Name : ", font=("times new roman",20),bg="red",fg="white").place(x=10,y=100)
        ent_Name = Entry(frame1, font=("times new roman",15),textvariable=self.var_stu_Name,bg="white",fg="black")
        ent_Name.place(x=200,y=100,width=200,height=30)

        lbl_f_name = Label(frame1,text="Father Name : ", font=("times new roman",20),bg="red",fg="white").place(x=10,y=140)
        ent_f_name = Entry(frame1, font=("times new roman",15),textvariable=self.var_stu_f_name,bg="white",fg="black")
        ent_f_name.place(x=200,y=140,width=200,height=30)

        lbl_m_name = Label(frame1,text="Mather Name : ", font=("times new roman",20),bg="red",fg="white").place(x=10,y=180)
        ent_m_name = Entry(frame1, font=("times new roman",15),textvariable=self.var_stu_m_name,bg="white",fg="black")
        ent_m_name.place(x=200,y=180,width=200,height=30)

        lbl_email = Label(frame1,text="Email : ", font=("times new roman",20),bg="red",fg="white").place(x=10,y=220)
        ent_email = Entry(frame1, font=("times new roman",15),textvariable=self.var_stu_email,bg="white",fg="black")
        ent_email.place(x=200,y=220,width=200,height=30)

        lbl_gender = Label(frame1,text="Gender : ", font=("times new roman",20),bg="red",fg="white").place(x=10,y=260)
        combo_gender = ttk.Combobox(frame1,font=('times new roman',14),state='readonly',justify=CENTER,textvariable=self.var_stu_gender)
        combo_gender['values']=['Male','Female','Other']
        combo_gender.place(x=200,y=260,width=200,height=30)
        combo_gender.current(0)

        lbl_contact = Label(frame1,text="Contact No : ", font=("times new roman",20),bg="red",fg="white").place(x=10,y=300)
        ent_contact = Entry(frame1, font=("times new roman",15),textvariable=self.var_stu_contact,bg="white",fg="black")
        ent_contact.place(x=200,y=300,width=200,height=30)

        lbl_dob = Label(frame1,text="D.O.B : ", font=("times new roman",20),bg="red",fg="white").place(x=10,y=340)
        ent_dob = Entry(frame1, font=("times new roman",15),textvariable=self.var_stu_dob,bg="white",fg="black")
        ent_dob.place(x=200,y=340,width=200,height=30)

        lbl_address = Label(frame1,text="Address : ", font=("times new roman",20),bg="red",fg="white").place(x=10,y=380)
        self.ent_address = Text(frame1, font=("times new roman",15),bg="white",fg="black")
        self.ent_address.place(x=200,y=380,width=200,height=100)



        ##################### btn ####################################################
        btn_add = Button(frame1,text='Add',command=self.add_students,font=('times new roman',18),bg='yellow',fg='black')
        btn_add.place(x=10,y=550,width=100,height=40)

        btn_update = Button(frame1,text='Update',command=self.update,font=('times new roman',18),bg='yellow',fg='black')
        btn_update.place(x=110,y=550,width=100,height=40)

        btn_delete = Button(frame1,text='Delete',command=self.delete_stu,font=('times new roman',18),bg='yellow',fg='black')
        btn_delete.place(x=210,y=550,width=100,height=40)

        btn_clear = Button(frame1,text='Clear',command=self.clear,font=('times new roman',18),bg='yellow',fg='black')
        btn_clear.place(x=310,y=550,width=100,height=40)


        ########################## Frame 2 #################################

        frame2 = Frame(self.root,bd=10,relief=RIDGE,bg='red').place(x=470,y=50,width=870,height=640)

        title2 = Label(frame2,text='Search By', font=('times new roman',20,'bold'),bg='red',fg='white').place(x=480,y=70)
     
        ########################## btn  ##################################

        self.combo_opption = ttk.Combobox(frame2,textvariable=self.var_stu_search_by,font=('times new roman',14),state='readonly',justify=CENTER,)
        self.combo_opption['values']=['Roll_No','Name','Contact']
        self.combo_opption.place(x=630,y=70,width=150,height=30)
        self.combo_opption.current(0)

        self.ent_blank = Entry(frame2,textvariable=self.var_stu_search_txt, font=("times new roman",15),bg="white",fg="black")
        self.ent_blank.place(x=800,y=70,width=150,height=30)

        self.btn_search = Button(frame2,text='Search',command=self.search_data, font=("times new roman",15),bg="white",fg="black")
        self.btn_search.place(x=970,y=70,width=150,height=30)

        self.btn_show = Button(frame2,text='Show All',command=self.fetch_data,font=("times new roman",15),bg="white",fg="black")
        self.btn_show.place(x=1140,y=70,width=150,height=30)

        ################# Frame 3 ####################################
        
        Table_Frame = Frame(frame2,bd=10,bg='white',relief=RIDGE)
        Table_Frame.place(x=490,y=120,width=830,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_Frame,columns=('Roll_no','Name','f_name','m_name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('Roll_no',text='Roll No.')
        self.student_table.heading('Name',text='Student Name')
        self.student_table.heading('f_name',text='Father Name')
        self.student_table.heading('m_name',text='Mother Name')
        self.student_table.heading('email',text='Email')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('contact',text='Contact')
        self.student_table.heading('dob',text='D.O.B')
        self.student_table.heading('address',text='Address')
        self.student_table['show']='headings'
        

        self.student_table.column('Roll_no',width=100)
        self.student_table.column('Name',width=100)
        self.student_table.column('f_name',width=100)
        self.student_table.column('m_name',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('contact',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('address',width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
      

    def add_students(self):
        if self.var_stu_roll.get()=='' or self.var_stu_gender.get()=='' or self.var_stu_contact.get()=='':
            messagebox.showerror("Error","Student details are required")
        else:
            try:
                con = pymysql.Connect(host='localhost',user='root',password='',db='student')
                cur = con.cursor()
                cur.execute("select * from stu_manage where Roll_no=%s",(self.var_stu_roll.get()))
                row = cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("Error","This Student ID has alredy available in our record try again with another ID")
                else:
                    cur.execute("insert into stu_manage values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_stu_roll.get(),self.var_stu_Name.get(),self.var_stu_f_name.get(),self.var_stu_m_name.get(),self.var_stu_email.get(),self.var_stu_gender.get(),self.var_stu_contact.get(),self.var_stu_dob.get(),self.ent_address.get('1.0',END)))
                    con.commit()
                    self.fetch_data()
                    self.clear()
                    con.close()
                    
                    messagebox.showinfo("Success","Record Added Successfully")                    
            
            except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")

    
    def fetch_data(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='student')
        cur = con.cursor()
        cur.execute("select * from stu_manage")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                con.commit()
        con.close()



    def clear(self):
        self.var_stu_roll.set('')
        self.var_stu_Name.set('')
        self.var_stu_f_name.set('')
        self.var_stu_m_name.set('')
        self.var_stu_email.set('')
        self.var_stu_gender.set('')
        self.var_stu_contact.set('')
        self.var_stu_dob.set('')
        self.ent_address.delete('1.0',END)

    

    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']
        self.var_stu_roll.set(row[0])
        self.var_stu_Name.set(row[1])
        self.var_stu_f_name.set(row[2])
        self.var_stu_m_name.set(row[3])
        self.var_stu_email.set(row[4])
        self.var_stu_gender.set(row[5])
        self.var_stu_contact.set(row[6])
        self.var_stu_dob.set(row[7])
        self.ent_address.delete('1.0',END)
        self.ent_address.insert(END,row[8])


    def update(self):
        if self.var_stu_roll.get()=='' or self.var_stu_contact.get()=='' or self.var_stu_email.get()=='':
            messagebox.showerror("Error","Student details are required")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='',database='student')
                cur = con.cursor()
                cur.execute("select * from stu_manage where Roll_no=%s",(self.var_stu_roll.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This Student ID is Invalid, try again with valid Student ID")
                else:
                    cur.execute("UPDATE `stu_manage` SET `Name`=%s,`f_name`=%s,`m_name`=%s,`email`=%s,`gender`=%s,`contact`=%s,`dob`=%s,`address`=%s WHERE `Roll_no`=%s",
                    (
                        
                        self.var_stu_Name.get(),
                        self.var_stu_f_name.get(),
                        self.var_stu_m_name.get(),
                        self.var_stu_email.get(),
                        self.var_stu_gender.get(),
                        self.var_stu_contact.get(),
                        self.var_stu_dob.get(),
                        self.ent_address.get('1.0',END),
                        self.var_stu_roll.get(),
                    )
                    )

                    con.commit()
                    self.fetch_data()
                    self.clear()
                    con.close()
                    
                    messagebox.showinfo("Success","Record Update Successfully")


            except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")




    def delete_stu(self):
        if self.var_stu_roll.get()=='':
            messagebox.showerror('Error','Student Id must be required')
        else:
            try:
                con = pymysql.Connect(host='localhost',user='root',password='',db='student')
                cur = con.cursor()
                cur.execute("select * from stu_manage where Roll_no=%s",(self.var_stu_roll.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student ID, please try again with another ID")
                else:
                    op = messagebox.askyesno("Confirm","Do You really want to delete")
                    if op == True:
                        cur.execute('delete from stu_manage where Roll_no=%s',(self.var_stu_roll.get()))
                        con.commit()
                        self.fetch_data()
                        con.close()
                        messagebox.showinfo("Delete",'Student Record Deleted Successfuly')
                        self.clear()
                    
            except Exception as ex:
                    messagebox.showerror(f"Error Due to{str(ex)}")


    def search_data(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='student')
        cur = con.cursor()
        cur.execute("SELECT * FROM `stu_manage` WHERE  "+str(self.var_stu_search_by.get())+" LIKE '%"+str(self.var_stu_search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                con.commit()
        con.close()

    
        



root = Tk()
obj = SchoolSystem(root)
root.mainloop()
