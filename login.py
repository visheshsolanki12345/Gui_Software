from tkinter import*
from tkinter import messagebox, ttk
import pymysql


class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed By Vishesh |")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fafafa')

################################## img add ##############################################
        self.phone_image=PhotoImage(file="image/phone1.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image, bd=0).place(x=100, y=10)





################################## Login Frame ##############################################


        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title=Label(login_frame, text='Login System', font=('Elephant',30,'bold'),bg='white').place(x=0, y=30, relwidth=1)


        ################################## Variable ##############################################

        self.var_f_name = StringVar()
        self.var_l_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_selcet_qutions = StringVar()
        self.var_combo_select_ans = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()

        lbl_user=Label(login_frame,text='Username', font=('Andalus',15),bg='white',fg='#767171').place(x=50, y=100)
        text_username = Entry(login_frame,font=("times new roman",15),textvariable=self.var_email,bg='#ECECEC').place(x=50, y=140, width=250)

        lbl_pass=Label(login_frame,text='Password', font=('Andalus',15),bg='white',fg='#767171').place(x=50, y=200)
        text_pass = Entry(login_frame,show='*',font=("times new roman",15),textvariable=self.var_confirm_password,bg='#ECECEC').place(x=50, y=240, width=250)

        btn_login=Button(login_frame, text="log In",command=self.main, font=('Arial Rounded MT Bold', 15), bg='#00B0F0',activebackground='#00B0F0', fg='white', activeforeground='white').place(x=50, y=300, width=250, height=35)

        hr=Label(login_frame, bg='lightgray').place(x=50, y=370, width=250, height=2)
        or_=Label(login_frame,text='OR',bg='white', fg='lightgray',font=('times new roman',15,'bold')).place(x=150, y=355)
 
        
        btn_forget=Button(login_frame, text='Forget Password?',command=self.forget_password, font=('times new roman',13),bg='white',fg='#00759E',bd=0,activebackground='white', activeforeground='#00759E').place(x=100, y=390)



################################## Frame 2 Register ##############################################

        register_frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        register_frame.place(x=650, y=570, width=350, height=75)

        lbl_reg=Label(register_frame, text=" New Register", font=('times new roman',13),bg='white').place(x=80, y=20)
        btn_signup=Button(register_frame, text='Sign Up ',command=self.regiration_windows,font=('times new roman',13,'bold'),bg='white',fg='#00759E',bd=0,activebackground='white', activeforeground='#00759E').place(x=200, y=20)




############################# Forget Password Main ###################################
    
    def clear(self):
        self.var_f_name.set('')
        self.var_l_name.set('')
        self.var_contact.set('')
        self.var_email.set('')
        self.var_combo_select_ans.set('')
        self.var_password.set('')
        self.var_confirm_password.set('')
       
        


    def forget_password_main(self):
        if self.var_combo_select_ans.get()=='Select' or self.var_selcet_qutions.get()=='' or self.var_confirm_password.get()=='':
            messagebox.showerror("Error",'All Fields are required')
        if self.var_confirm_password.get() != self.var_password.get():
            messagebox.showerror("Error","Password Should Be Same")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='login')
                cur = con.cursor()
                cur.execute("select * from login_system where email=%s and s_qutions=%s and s_ans=%s ",(self.var_email.get(),self.var_selcet_qutions.get(), self.var_combo_select_ans.get()))

                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",'Your Security Question is Wrong') 
                else:
                    cur.execute("UPDATE `login_system` SET `password`=%s, `confirm_password`=%s WHERE `email`=%s",
                    (
                        
                        self.var_confirm_password.get(),
                        self.var_password.get(),
                        self.var_email.get()
                    )
                    )

                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password Changed")
                    self.clear()
                    self.root.destroy()
                    import login

            except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")  



############################# Email Connecting ##############################################
    
    def forget_password(self):
        if self.var_email.get()=='':
            messagebox.showerror("Error","Please Enter Email")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='login')
                cur = con.cursor()
                cur.execute("select * from login_system where email=%s" ,(self.var_email.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",'Invalid Email') 
                else:
                    con.commit()
                    con.close() 
                    
                    
                    


  ################################## Second Window codeing ##############################################     
       
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x530+650+120")
                    self.root2.config(bg='white')
                    self.root2.focus_force()
                    self.root2.grab_set()

                    title_pass = Label(self.root2, text='Forget Password',font=('times new roman',30,'bold'),fg='black',bg='white').place(x=30,y=10)




################################## Label And Entry for Password Reset ##############################################

                    lbl_select_qutions = Label(self.root2,text='Select Security Questions',font=('times new roman',17),fg='black',bg='white').place(x=30,y=80)
                    self.combo_questions = ttk.Combobox(self.root2,font=('times new roman',15),textvariable=self.var_selcet_qutions,state='readonly',justify=CENTER,)
                    self.combo_questions['values']=["Select","Your First Pet Name","Your Birth Place","Your Best Friend Name"]
                    self.combo_questions.place(x=30,y=120,width=250,height=25)
                    self.combo_questions.current(0)

                    lbl_select_ans = Label(self.root2,text='Security Answer',font=('times new roman',17),fg='black',bg='white').place(x=30,y=155)
                    self.ent_select_ans = Entry(self.root2,bd=1,font=('times new roman',15),textvariable=self.var_combo_select_ans,fg='black',bg='lightyellow')
                    self.ent_select_ans.place(x=30,y=190,width=250,height=25)

                    lbl_password = Label(self.root2,text='New Password',font=('times new roman',17),fg='black',bg='white').place(x=30,y=220)
                    self.ent_password = Entry(self.root2,bd=1,font=('times new roman',17),textvariable=self.var_password,fg='black',bg='lightyellow')
                    self.ent_password.place(x=30,y=260,width=250,height=25)

                    lbl_confirm_password = Label(self.root2,text='Confirm Password',font=('times new roman',15),fg='black',bg='white').place(x=30,y=295)
                    self.ent_confirm_password = Entry(self.root2,bd=1,font=('times new roman',15),textvariable=self.var_confirm_password,fg='black',bg='lightyellow')
                    self.ent_confirm_password.place(x=30,y=330,width=250,height=25)
                    
                    btn_save_password = Button(self.root2,text='Reset Password',command=self.forget_password_main,font=('times new roman',20),fg='white',bg='green',).place(x=55,y=380,width=200,height=30)
            
            except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")


            
################################## Regiration Window code ##############################################

    def regiration_windows(self):
        self.root.destroy()
        import login1


################################## Username And Password Login ##############################################

    def main(self):
        if self.var_email.get()=='':
            messagebox.showerror("Error","Please Fill Email ID")
        elif self.var_confirm_password.get()=='':
            messagebox.showerror("Error","Please Fill Password ")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='login')
                cur = con.cursor()
                cur.execute("select * from login_system where email=%s and confirm_password=%s" ,(self.var_email.get(),self.var_confirm_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",'Invalid Username & password') 
                else:
                    messagebox.showinfo("Success","Login  Successfully")
    
                    self.root.destroy()
                    import button_frame
                    
                con.commit()
                con.close()
                self.clear()


            except Exception as ex:
                messagebox.showerror(f"Error Due to : {str(ex)}")
    



################################## Clear FUNCTION ##############################################

    

    
root=Tk()
obj = Login_System(root)
root.mainloop()
