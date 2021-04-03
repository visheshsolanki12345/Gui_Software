from tkinter import*
from tkinter import messagebox, ttk
import pymysql
import time 
import os 
import tempfile

class EmployeeSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Employee Payroll Management System | Developer By VISHESH")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')
        title = Label(self.root,text="Employee Payroll Management System", font=("times new roman",25,"bold"),bg="blue",fg="white",anchor="w",padx=10).place(x=0,y=0, relwidth=1)
        btn_emp = Button(self.root,text="All Employee's",command=self.Employee_freme,font=("times new roman",13,),bg="white",fg="black").place(x=1100,y=10, width=130, height=28)
        
        
        ########### Frame 1 ###############################
        ########### Variable ##############################
        self.var_emp_code = StringVar()
        self.var_emp_designation = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_age = StringVar()
        self.var_emp_gender = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_location = StringVar()
        self.var_emp_dob = StringVar()
        self.var_emp_exprience = StringVar()    
        self.var_emp_doj = StringVar()
        self.var_emp_proof = StringVar() ####### Adhar Card
        self.var_emp_contact = StringVar()
        self.var_emp_status = StringVar()    


        Frame1 = Frame(self.root,bd=5,relief=RIDGE, bg='white')
        Frame1.place(x=10,y=70,width=750,height=620)
        title2 = Label(Frame1,text="Employee Details", font=("times new roman",15),bg="yellow",fg="black",anchor="w",padx=10).place(x=0,y=0, relwidth=1)

        ########## Search #################################
        lbl_code = Label(Frame1,text="Employee Code", font=("times new roman",15),bg="green",fg="white").place(x=10,y=50)
        self.lbl_code = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_code,bg="lightyellow",fg="black")
        self.lbl_code.place(x=200,y=50, width=300)
        lbl_code = Button(Frame1,text="Search",command=self.search, font=("times new roman",15),bg="lightpink",fg="black").place(x=520,y=50, width=100, height=28)


        ######### Row 1 #################################
        lbl_designation = Label(Frame1,text="Designation : ", font=("times new roman",15),bg="white",fg="black").place(x=10,y=100)
        lbl_designation = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_designation,bg="lightyellow",fg="black").place(x=150,y=100, width=200)
        lbl_doj = Label(Frame1,text="D.O.J", font=("times new roman",15),bg="white",fg="black").place(x=400,y=100)
        lbl_doj = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_doj,bg="lightyellow",fg="black").place(x=500,y=100)


        ######### Row 2 #################################
        lbl_name = Label(Frame1,text="Name : ", font=("times new roman",15),bg="white",fg="black").place(x=10,y=150)
        lbl_name = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_name,bg="lightyellow",fg="black").place(x=150,y=150, width=200)
        lbl_dob = Label(Frame1,text="D.O.B", font=("times new roman",15),bg="white",fg="black").place(x=400,y=150)
        lbl_dob = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_dob,bg="lightyellow",fg="black").place(x=500,y=150)

        ######### Row 3 #################################
        lbl_age = Label(Frame1,text="Age : ", font=("times new roman",15),bg="white",fg="black").place(x=10,y=200)
        lbl_age = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_age,bg="lightyellow",fg="black").place(x=150,y=200, width=200)
        lbl_experience = Label(Frame1,text="Experience: ", font=("times new roman",15),bg="white",fg="black").place(x=400,y=200)
        lbl_experience = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_exprience,bg="lightyellow",fg="black").place(x=500,y=200)

        ######### Row 4 #################################
        lbl_gender = Label(Frame1,text="Gender : ", font=("times new roman",15),bg="white",fg="black").place(x=10,y=250)
        lbl_gender = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_gender,bg="lightyellow",fg="black").place(x=150,y=250, width=200)
        lbl_proof = Label(Frame1,text="Proof ID : ", font=("times new roman",15),bg="white",fg="black").place(x=400,y=250)
        lbl_proof = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_proof,bg="lightyellow",fg="black").place(x=500,y=250)

        ######### Row 5 ################################
        lbl_email = Label(Frame1,text="Email : ", font=("times new roman",15),bg="white",fg="black").place(x=10,y=300)
        lbl_email = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_email,bg="lightyellow",fg="black").place(x=150,y=300, width=200)
        lbl_contact = Label(Frame1,text="Contact No.", font=("times new roman",15),bg="white",fg="black").place(x=400,y=300)
        lbl_contact = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_contact,bg="lightyellow",fg="black").place(x=500,y=300)

        ######## Row 6 ###############################
        lbl_location = Label(Frame1,text="H.Location : ", font=("times new roman",15),bg="white",fg="black").place(x=10,y=350)
        lbl_location = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_location,bg="lightyellow",fg="black").place(x=150,y=350, width=200)
        lbl_status = Label(Frame1,text="Status : ", font=("times new roman",15),bg="white",fg="black").place(x=400,y=350)
        lbl_status = Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp_status,bg="lightyellow",fg="black").place(x=500,y=350)


        ########## Address 7##########################
        self.lbl_address = Label(Frame1,text="Address : ", font=("times new roman",15),bg="white",fg="black").place(x=10,y=400)
        self.lbl_address = Text(Frame1, font=("times new roman",15,),bg="lightyellow",fg="black")
        self.lbl_address.place(x=150,y=400, width=555,height=170)


        ########### Frame 2 ###############################
        ########### Variable ##############################
        self.var_emp_month = StringVar()
        self.var_emp_year = StringVar()
        self.var_emp_bas_salary = StringVar()
        self.var_emp_days = StringVar()
        self.var_emp_absents = StringVar()
        self.var_emp_medical = StringVar()
        self.var_emp_fund = StringVar()
        self.var_emp_convence = StringVar()
        self.var_emp_netsalary = StringVar()
        
        

        Frame2 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)
        title2 = Label(Frame2,text="Salary Details", font=("times new roman",15,),bg="yellow",fg="black",anchor="w",padx=10).place(x=0,y=0, relwidth=1)


        ########## Row 1 ##################################

        lbl_month = Label(Frame2,text="Month:", font=("times new roman",15,),bg="white",fg="black").place(x=5,y=50)
        lbl_month = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_month,bg="lightyellow",fg="black").place(x=70,y=50, width=100)
        lbl_year = Label(Frame2,text="Year:", font=("times new roman",15,),bg="white",fg="black").place(x=190,y=50)
        lbl_year = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_year,bg="lightyellow",fg="black").place(x=245,y=50, width=100)
        lbl_bas_salary = Label(Frame2,text="Bas.Salary:", font=("times new roman",15,),bg="white",fg="black").place(x=365,y=50)
        lbl_bas_salary = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_bas_salary,bg="lightyellow",fg="black").place(x=470,y=50, width=100)

        ######### Row 2 ###################################
        lbl_days = Label(Frame2,text="Total Days : ", font=("times new roman",15,),bg="white",fg="black").place(x=5,y=80)
        lbl_days = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_days,bg="lightyellow",fg="black").place(x=120,y=80, width=100)
        lbl_absents = Label(Frame2,text="Absents : ", font=("times new roman",15,),bg="white",fg="black").place(x=250,y=80)
        lbl_absents = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_absents,bg="lightyellow",fg="black").place(x=340,y=80, width=100)

        ######### Row 3 ###################################
        lbl_medical = Label(Frame2,text="Medical : ", font=("times new roman",15,),bg="white",fg="black").place(x=5,y=140)
        lbl_medical = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_medical,bg="lightyellow",fg="black").place(x=100,y=140, width=150)
        lbl_fund = Label(Frame2,text="Provident Fund : ", font=("times new roman",15,),bg="white",fg="black").place(x=270,y=140)
        lbl_fund = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_fund,bg="lightyellow",fg="black").place(x=420,y=140, width=150)


        ######### Row 4 ##################################
        lbl_convence = Label(Frame2,text="Convence : ", font=("times new roman",15,),bg="white",fg="black").place(x=5,y=170)
        lbl_convence = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_convence,bg="lightyellow",fg="black").place(x=100,y=170, width=150)
        lbl_netsalary = Label(Frame2,text="Net Salary : ", font=("times new roman",15,),bg="white",fg="black").place(x=270,y=170)
        lbl_netsalary = Entry(Frame2, font=("times new roman",15),textvariable=self.var_emp_netsalary,bg="lightyellow",fg="black").place(x=420,y=170, width=150)
        
        ######### Button ################################
        lbl_calcuate = Button(Frame2,text="Calcuate",command=self.calculate,font=("times new roman",15,),bg="green",fg="black").place(x=250,y=210, width=100, height=28)
        self.lbl_save = Button(Frame2,text="Save",command=self.add, font=("times new roman",15,),bg="gray",fg="black")
        self.lbl_save.place(x=350,y=210, width=100, height=28)
        lbl_clear = Button(Frame2,text="Clear",command=self.clear, font=("times new roman",15),bg="orange",fg="black").place(x=450,y=210, width=100, height=28)
        self.lbl_delete = Button(Frame2,text="Delete",state=DISABLED,command=self.delete, font=("times new roman",15),bg="red",fg="white")
        self.lbl_delete.place(x=400,y=240, width=150, height=28)
        self.lbl_update = Button(Frame2,text="Update",state=DISABLED,command=self.update, font=("times new roman",15),bg="blue",fg="white")
        self.lbl_update.place(x=250,y=240, width=150, height=28)

        
        ########### Frame 3 ###############################
        Frame3 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)

        ########## Calculater #############################
        self.var_txt = StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator = self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
        
        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator = ''




        cal_Frame = Frame(Frame3,bg='white',bd=2,relief=RIDGE)
        cal_Frame.place(x=2,y=2,width=246,height=300)
        
        txt_result = Entry(cal_Frame, bg='orange',textvariable=self.var_txt,font=("times new roman",20,'bold'),justify=RIGHT).place(x=0,y=0,height=50,relwidth=1,)
        
        ######### Row 1 ##################################
        btn_7 = Button(cal_Frame,text='7',command=lambda:btn_click(7),font=('times new roman',15,'bold')).place(x=0,y=52,w=60,h=60)
        btn_8 = Button(cal_Frame,text='8',command=lambda:btn_click(8), font=('times new roman',15,'bold')).place(x=61,y=52,w=60,h=60)
        btn_9 = Button(cal_Frame,text='9',command=lambda:btn_click(9), font=('times new roman',15,'bold')).place(x=122,y=52,w=60,h=60)
        btn_div = Button(cal_Frame,text='/',command=lambda:btn_click('/'), font=('times new roman',15,'bold')).place(x=183,y=52,w=60,h=60)

        ######## Row 2 ###################################
        btn_4 = Button(cal_Frame,text='4',command=lambda:btn_click(4), font=('times new roman',15,'bold')).place(x=0,y=112,w=60,h=60)
        btn_5 = Button(cal_Frame,text='5',command=lambda:btn_click(5), font=('times new roman',15,'bold')).place(x=61,y=112,w=60,h=60)
        btn_6 = Button(cal_Frame,text='6',command=lambda:btn_click(6), font=('times new roman',15,'bold')).place(x=122,y=112,w=60,h=60)
        btn_mul = Button(cal_Frame,text='*',command=lambda:btn_click('*'), font=('times new roman',15,'bold')).place(x=183,y=112,w=60,h=60)

        ####### Row 3 #####################################
        btn_1 = Button(cal_Frame,text='1',command=lambda:btn_click(1), font=('times new roman',15,'bold')).place(x=0,y=172,w=60,h=60)
        btn_2 = Button(cal_Frame,text='2',command=lambda:btn_click(2), font=('times new roman',15,'bold')).place(x=61,y=172,w=60,h=60)
        btn_3 = Button(cal_Frame,text='3',command=lambda:btn_click(3), font=('times new roman',15,'bold')).place(x=122,y=172,w=60,h=60)
        btn_min = Button(cal_Frame,text='-',command=lambda:btn_click('-'), font=('times new roman',15,'bold')).place(x=183,y=172,w=60,h=60)

        ####### Row 4 #####################################
        btn_0 = Button(cal_Frame,text='0',command=lambda:btn_click('0'), font=('times new roman',15,'bold')).place(x=0,y=232,w=60,h=60)
        btn_dot = Button(cal_Frame,text='Clear',command=clear_cal, font=('times new roman',15,'bold')).place(x=61,y=232,w=60,h=60)
        btn_sum = Button(cal_Frame,text='+',command=lambda:btn_click('+',), font=('times new roman',15,'bold')).place(x=122,y=232,w=60,h=60)
        btn_equal = Button(cal_Frame,text='=',command=result, font=('times new roman',15,'bold')).place(x=183,y=232,w=60,h=60)


        ####### Salary Print #############################
        sal_Frame = Frame(Frame3,bg='white',bd=2,relief=RIDGE)
        sal_Frame.place(x=251,y=2,width=320,height=300)

        title_sal = Label(sal_Frame,text="Salary Reciept", font=("times new roman",15,),bg="yellow",fg="black",anchor="w",padx=10).place(x=0,y=0, relwidth=1)

        sal_Frame2 = Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)


####################### Salary Receipt ################################
        self.sample = '''\tCompany Name, xyz\n\tAddress: Xyz, Floor4
------------------------------------------------
Employee ID\t\t:  
Salary of\t\t:  MON YYYY
Generated On\t\t:  DD-MM-YYYY
------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Convence\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Gross Payment\t\t:  Rs.------
Net salary\t\t:  Rs.------
------------------------------------------------
This is computer generated slip, not 
required any signature
'''

        scroll_y = Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_recipt = Text(sal_Frame2, font=("times new roman",13),bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END,self.sample)



        self.lbl_print = Button(sal_Frame,text="Print",state=DISABLED,command=self.print, font=("times new roman",15),bg="lightblue",fg="black")
        self.lbl_print.place(x=120,y=262, width=100, height=28)


############################## check Connection #####################

        #self.check_connection()

######################## ALL FUNCTION START HERE #####################################

    def calculate(self):
        if self.var_emp_month.get()=='' or self.var_emp_year.get()=='' or self.var_emp_bas_salary.get()=='':
            messagebox.showerror("Error","All fields are required")
        else:
            per_day = int(self.var_emp_bas_salary.get())/int(self.var_emp_days.get())
            work_day = int(self.var_emp_days.get())-int(self.var_emp_absents.get())
            sal_ = per_day*work_day
            deduct = int(self.var_emp_medical.get())+int(self.var_emp_fund.get())
            addition = int(self.var_emp_convence.get())
            net_sal = sal_ - deduct + addition
            self.var_emp_netsalary.set(str(round(net_sal,2)))

######################## Updata The Salary Receipt ################################
            new_sample = f'''\tCompany Name, xyz\n\tAddress: Xyz, Floor4
------------------------------------------------
Employee ID\t\t:  {self.var_emp_code.get()}
Salary of\t\t:  {self.var_emp_code.get()}-{self.var_emp_year.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
------------------------------------------------
Total Days\t\t:  {self.var_emp_days.get()}
Total Present\t\t:  {str(int(self.var_emp_days.get())-int(self.var_emp_absents.get()))}
Total Absent\t\t:  {self.var_emp_absents.get()}
Convence\t\t:  Rs.{self.var_emp_convence.get()}
Medical\t\t:  Rs.{self.var_emp_medical.get()}
PF\t\t:  Rs.{self.var_emp_fund.get()}
Gross Payment\t\t: Rs.{self.var_emp_bas_salary.get()}
Net salary\t\t: Rs.{self.var_emp_netsalary.get()}
------------------------------------------------
This is computer generated slip, not 
required any signature
'''
            self.txt_salary_recipt.delete('1.0',END)
            self.txt_salary_recipt.insert(END,new_sample)

    ######### Frem 1 Variable ################
    def search(self):
        try:
            con = pymysql.Connect(host='localhost',user='root',password='',db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            row = cur.fetchone()
            #print(rows)
            if row==None:
                messagebox.showerror("Error","Invalid Employee ID, please try again with another ID")
            else:
                self.var_emp_code.set(row[0])
                self.var_emp_designation.set(row[1])
                self.var_emp_name.set(row[2])
                self.var_emp_age.set(row[3])
                self.var_emp_gender.set(row[4])
                self.var_emp_email.set(row[5])
                self.var_emp_location.set(row[6])
                self.var_emp_doj.set(row[7])
                self.var_emp_dob.set(row[8])
                self.var_emp_exprience.set(row[9])   
                self.var_emp_proof.set(row[10])
                self.var_emp_contact.set(row[11])
                self.var_emp_status.set(row[12])
                self.lbl_address.delete('1.0',END)
                self.lbl_address.insert(END,row[13])
                self.var_emp_month.set(row[14])
                self.var_emp_year.set(row[15])
                self.var_emp_bas_salary.set(row[16])
                self.var_emp_days.set(row[17])
                self.var_emp_absents.set(row[18])
                self.var_emp_medical.set(row[19])
                self.var_emp_fund.set(row[20])
                self.var_emp_convence.set(row[21])
                self.var_emp_netsalary.set(row[22])
                file_ = open("Salary_reciept/"+str(row[23]),"r")
                self.txt_salary_recipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_recipt.insert(END,i)
                file_.close()
                self.lbl_save.config(state=DISABLED)
                self.lbl_delete.config(state=NORMAL)
                self.lbl_update.config(state=NORMAL)
                self.lbl_code.config(state='readonly')
                self.lbl_print.config(state=NORMAL)
                
        except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")
    



    def clear(self):
        
        self.lbl_save.config(state=NORMAL)
        self.lbl_delete.config(state=DISABLED)
        self.lbl_update.config(state=DISABLED)
        self.lbl_print.config(state=DISABLED)
        self.lbl_code.config(state=NORMAL)

        self.var_emp_code.set('')
        self.var_emp_designation.set('')
        self.var_emp_name.set('')
        self.var_emp_age.set('')
        self.var_emp_gender.set('')
        self.var_emp_email.set('')
        self.var_emp_location.set('')
        self.var_emp_doj.set('')
        self.var_emp_dob.set('')
        self.var_emp_exprience.set('')   
        self.var_emp_proof.set('')
        self.var_emp_contact.set('')
        self.var_emp_status.set('')
        self.lbl_address.delete('1.0',END)
        self.var_emp_month.set('')
        self.var_emp_year.set('')
        self.var_emp_bas_salary.set('')
        self.var_emp_days.set('')
        self.var_emp_absents.set('')
        self.var_emp_medical.set('')
        self.var_emp_fund.set('')
        self.var_emp_convence.set('')
        self.var_emp_netsalary.set('')
        self.txt_salary_recipt.delete('1.0',END)
        self.txt_salary_recipt.insert(END,self.sample)




    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror('Error','Employee Id must be required')
        else:
            try:
                con = pymysql.Connect(host='localhost',user='root',password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row = cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, please try again with another ID")
                else:
                    op = messagebox.askyesno("Confirm","Do You really want to delete")
                    if op == True:
                        cur.execute('delete from emp_salary where e_id=%s',(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete",'Employee Record Deleted Successfuly')
                        self.clear()
                    
            except Exception as ex:
                    messagebox.showerror(f"Error Due to : {str(ex)}")
    


    def add(self):
        if self.var_emp_code.get()=='' or self.var_emp_netsalary.get()=='' or self.var_emp_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:

            try:
                con = pymysql.Connect(host='localhost',user='root',password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row = cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("Error","This Employee ID has alredy available in our record try again with another ID")
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

                    (
    
                        self.var_emp_code.get(),
                        self.var_emp_designation.get(),
                        self.var_emp_name.get(),
                        self.var_emp_age.get(),
                        self.var_emp_gender.get(),
                        self.var_emp_email.get(),
                        self.var_emp_location.get(),
                        self.var_emp_doj.get(),
                        self.var_emp_dob.get(),
                        self.var_emp_exprience.get(),   
                        self.var_emp_proof.get(),
                        self.var_emp_contact.get(),
                        self.var_emp_status.get(),
                        self.lbl_address.get('1.0',END),
                        self.var_emp_month.get(),
                        self.var_emp_year.get(),
                        self.var_emp_bas_salary.get(),
                        self.var_emp_days.get(),
                        self.var_emp_absents.get(),
                        self.var_emp_medical.get(),
                        self.var_emp_fund.get(),
                        self.var_emp_convence.get(),
                        self.var_emp_netsalary.get(),
                        self.var_emp_code.get()+".txt"
                        

                    )
                    )
                    con.commit()
                    con.close()


                    file_ = open("Salary_reciept/"+str(self.var_emp_code.get())+".txt","w")
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close()


                    messagebox.showinfo("Success","Record Added Successfully")
                    self.lbl_print.config(state=NORMAL)

                    
            except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")

    

    def update(self):
        if self.var_emp_code.get()=='' or self.var_emp_netsalary.get()=='' or self.var_emp_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:

            try:
                con = pymysql.Connect(host='localhost',user='root',password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row = cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","This Employee ID is Invalid, try again with valid Employee ID")
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`salary`=%s,`days`=%s,`abbsent`=%s,`medical`=%s,`found`=%s,`convence`=%s,`netsalary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",
                    (
                    
                        self.var_emp_designation.get(),
                        self.var_emp_name.get(),
                        self.var_emp_age.get(),
                        self.var_emp_gender.get(),
                        self.var_emp_email.get(),
                        self.var_emp_location.get(),
                        self.var_emp_doj.get(),
                        self.var_emp_dob.get(),
                        self.var_emp_exprience.get(),   
                        self.var_emp_proof.get(),
                        self.var_emp_contact.get(),
                        self.var_emp_status.get(),
                        self.lbl_address.get('1.0',END),
                        self.var_emp_month.get(),
                        self.var_emp_year.get(),
                        self.var_emp_bas_salary.get(),
                        self.var_emp_days.get(),
                        self.var_emp_absents.get(),
                        self.var_emp_medical.get(),
                        self.var_emp_fund.get(),
                        self.var_emp_convence.get(),
                        self.var_emp_netsalary.get(),
                        self.var_emp_code.get()+".txt",
                        self.var_emp_code.get(),
                    )
                    )    

                    
                    
                    con.commit()
                    con.close()


                    file_ = open("Salary_reciept/"+str(self.var_emp_code.get())+".txt","w")
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close()


                    messagebox.showinfo("Success","Record Update Successfully")

                    
            except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")



        ########### Database Connection ###########
    # def check_connection(self):
            
        try:
            con = pymysql.Connect(host='localhost',user='root',password='',db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary")
            rows = cur.fetchall()
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")

    
    def show(self):    
        try:
            con = pymysql.Connect(host='localhost',user='root',password='',db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary")
            rows = cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}")
        


    def Employee_freme(self):
        self.root2 = Toplevel()
        self.root2.title("Employee Payroll Management System | Developer By VISHESH")
        self.root2.geometry("900x500+100+100")
        self.root2.config(bg='white')
        title = Label(self.root2,text="All Employee Details ", font=("times new roman",25,"bold"),bg="black",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()

        scroll_x = Scrollbar(self.root2,orient=HORIZONTAL)
        scroll_y = Scrollbar(self.root2,orient=VERTICAL)
        
        self.employee_tree = ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'location', 'doj', 'dob', 'experience', 'proof', 'contact', 'status', 'address', 'month', 'year', 'salary', 'days', 'abbsent', 'medical', 'found', 'convence', 'netsalary', 'salary_receipt'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_tree.xview)
        scroll_y.config(command=self.employee_tree.yview)

        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('location',text='Location')
        self.employee_tree.heading('doj',text='D.O.J')
        self.employee_tree.heading('dob',text='D.O.B')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof',text='Proof')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('salary',text='Salary')
        self.employee_tree.heading('days',text='Days')
        self.employee_tree.heading('abbsent',text='Abbsent')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('found',text='Found')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('netsalary',text='Netsalary')
        self.employee_tree.heading('salary_receipt',text='Salary_Receipt')
        
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=100)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('salary',width=100)
        self.employee_tree.column('days',width=100)
        self.employee_tree.column('abbsent',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('found',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('netsalary',width=100)
        self.employee_tree.column('salary_receipt',width=100)
        

        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        self.root2.mainloop()

    def print(self):
        
        file_ = tempfile.mktemp(".txt")
        open(file_,"w").write(self.txt_salary_recipt.get('1.0',END))
        os.startfile(file_,'print')

root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
