from tkinter import*
#from PIL import Image,ImageTk
from tkinter import messagebox, ttk
import pymysql

class Regiseration():
    def __init__(self,root):
        self.root = root
        self.root.title("Regiseration Form")
        self.root.geometry("1350x700+0+0")

        ############# bg Images   ##############
        self.bg=PhotoImage(file="login/image1.png")
        bg=Label(self.root,image=self.bg, bd=0).place(x=200, y=0, relwidth=1, relheight=1)

        self.left=PhotoImage(file="login/image2.png")
        left=Label(self.root,image=self.left, bd=0).place(x=100, y=100,width=450, height=400)

        reg_btn = Button(self.root,text='Sign In',command=self.login_windows,font=('times new roman',17,'bold'),fg='black',bg='white')
        reg_btn.place(x=200,y=465,width=210,height=30)

        ############ Regiseration Frame ##################

        frame1 = Frame(self.root,bg='white') 
        frame1.place(x=550,y=100,width=700,height=400)
        
        title1 = Label(frame1,text='REGISTER HERE',font=('times new roman',20,'bold'),fg='green',bg='white').place(x=40,y=5)

        self.var_f_name = StringVar()
        self.var_l_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_selcet_qutions = StringVar()
        self.var_combo_select_ans = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()


        lbl_first_name = Label(frame1,text='First Name',font=('times new roman',15),fg='black',bg='white').place(x=40,y=60)
        self.ent_first_name = Entry(frame1,textvariable=self.var_f_name,bd=1,font=('times new roman',15),fg='black',bg='lightyellow')
        self.ent_first_name.place(x=40,y=90,width=250,height=25)

        lbl_last_name = Label(frame1,text='Last Name',font=('times new roman',15),fg='black',bg='white').place(x=400,y=60)
        self.ent_last_name = Entry(frame1,bd=1,font=('times new roman',15),textvariable=self.var_l_name,fg='black',bg='lightyellow')
        self.ent_last_name.place(x=400,y=90,width=250,height=25)

        lbl_contact = Label(frame1,text='Contact',font=('times new roman',15),fg='black',bg='white').place(x=40,y=120)
        self.ent_contact = Entry(frame1,bd=1,font=('times new roman',15),textvariable=self.var_contact,fg='black',bg='lightyellow')
        self.ent_contact.place(x=40,y=150,width=250,height=25)

        lbl_email = Label(frame1,text='Email',font=('times new roman',15),fg='black',bg='white').place(x=400,y=120)
        self.ent_email = Entry(frame1,bd=1,font=('times new roman',15),textvariable=self.var_email,fg='black',bg='lightyellow')
        self.ent_email.place(x=400,y=150,width=250,height=25)

        lbl_select_qutions = Label(frame1,text='Select Security Questions',font=('times new roman',15),fg='black',bg='white').place(x=40,y=180)
        self.combo_questions = ttk.Combobox(frame1,font=('times new roman',15),state='readonly',justify=CENTER,textvariable=self.var_selcet_qutions)
        self.combo_questions['values']=["Select","Your First Pet Name","Your Birth Place","Your Best Friend Name"]
        self.combo_questions.place(x=40,y=210,width=250,height=25)
        self.combo_questions.current(0)

        lbl_select_ans = Label(frame1,text='Security Answer',font=('times new roman',15),fg='black',bg='white').place(x=400,y=180)
        self.ent_select_ans = Entry(frame1,bd=1,font=('times new roman',15),textvariable=self.var_combo_select_ans,fg='black',bg='lightyellow')
        self.ent_select_ans.place(x=400,y=210,width=250,height=25)

        lbl_password = Label(frame1,text='Password',font=('times new roman',15),fg='black',bg='white').place(x=40,y=240)
        self.ent_password = Entry(frame1,bd=1,font=('times new roman',15),textvariable=self.var_password,fg='black',bg='lightyellow')
        self.ent_password.place(x=40,y=270,width=250,height=25)

        lbl_confirm_password = Label(frame1,text='Confirm Password',font=('times new roman',15),fg='black',bg='white').place(x=400,y=240)
        self.ent_confirm_password = Entry(frame1,bd=1,font=('times new roman',15),textvariable=self.var_confirm_password,fg='black',bg='lightyellow')
        self.ent_confirm_password.place(x=400,y=270,width=250,height=25)

        self.var_chk = IntVar()
        chk = Checkbutton(frame1,text='I Agree The Terms & Conditins',variable=self.var_chk,onvalue=1, offvalue=0, font=('times new roman',13),fg='red',bg='lightyellow').place(x=40,y=320)

        reg_btn = Button(frame1,text='REGISTER NOW',command=self.add,font=('times new roman',17,'bold'),fg='white',bg='green')
        reg_btn.place(x=40,y=360,width=250,height=25)

    

    def clear(self):
        self.var_f_name.set('')
        self.var_l_name.set('')
        self.var_contact.set('')
        self.var_email.set('')
        self.var_combo_select_ans.set('')
        self.var_password.set('')
        self.var_confirm_password.set('')
        self.combo_questions.current(0)
        
        
    def login_windows(self):
        self.root.destroy()
        import login


    def add(self):
        if self.var_f_name.get()=='':
            messagebox.showerror("Error","Please Fill First Name")
        if self.var_l_name.get()=='':
            messagebox.showerror("Error","please Fill Last Name")
        if self.var_contact.get()=='':
            messagebox.showerror("Error","Please fill Contact")
        if self.var_email.get()=='':
            messagebox.showerror("Error","Please Fill Email ID")
        if self.var_selcet_qutions.get()=='':
            messagebox.showerror("Error","Please Fill Security Questions")
        if self.var_combo_select_ans.get()=='':
            messagebox.showerror("Error","Please Fill Security Answer")
        if self.var_password.get()=='':
            messagebox.showerror("Error","Please Fill Password")
        if self.var_confirm_password.get()=='':
            messagebox.showerror("Error","Please Fill Confirm Password")
        if self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error",'Password & Confirm Password Should be Same')
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Conditions")
        else:
            try:
                con = pymysql.Connect(host='localhost',user='root',password='',db='login')
                cur = con.cursor()
                cur.execute("select * from login_system where email=%s",(self.var_email.get()))
                row = cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("Error","This Email ID alredy available in our record")
                else:
                    cur.execute("insert into login_system values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_f_name.get(),self.var_l_name.get(),self.var_contact.get(),self.var_email.get(),self.var_selcet_qutions.get(),self.var_combo_select_ans.get(),self.var_password.get(),self.var_confirm_password.get(),))
                    con.commit()
                    con.close()
                    
                    
                    messagebox.showinfo("Success","Regiseration  Successfully")
                    self.clear()
                    self.root.destroy()
                    import login
                    
                    
                        
            
            except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")
                

root = Tk()
obj = Regiseration(root)
root = mainloop()


