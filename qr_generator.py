from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title('QR Generator | Developed By Vishesh')
        # self.root.resizable(False,False)

        title_main = Label(self.root,text="QR Generator",font=("times new roman",30,'bold'),bg='blue',fg='white',anchor="w",padx=1,).place(x=5,y=5,relwidth=1)


        ################### Frame 1 ##############################################
        ################### Variable #############################################
        
        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_department = StringVar()
        self.var_emp_designation = StringVar()

        frame1 = Frame(self.root,bd=10,relief=RIDGE,bg='white')
        frame1.place(x=50,y=80,width=500,height=350)

        title1 = Label(frame1,text='Employee Details',font=('times new roman',20,'bold'),fg='black',bg='yellow',).place(x=0,y=0,relwidth=1)
        
        lbl_code = Label(frame1,text='Employee ID : ', font=('times new roman',15),fg='black', bg='white').place(x=10,y=50)
        ent_code = Entry(frame1,font=('times new roman',15),textvariable=self.var_emp_code,bg='lightyellow',fg='black')
        ent_code.place(x=200,y=55,width=200)

        lbl_name = Label(frame1,text='Name : ', font=('times new roman',15),fg='black', bg='white').place(x=10,y=100)
        ent_name = Entry(frame1,font=('times new roman',15),textvariable=self.var_emp_name,bg='lightyellow',fg='black')
        ent_name.place(x=200,y=100,width=200)

        lbl_department = Label(frame1,text='Department : ', font=('times new roman',15),fg='black', bg='white').place(x=10,y=150)
        ent_department = Entry(frame1,font=('times new roman',15),textvariable=self.var_emp_department,bg='lightyellow',fg='black')
        ent_department.place(x=200,y=150,width=200)

        lbl_designation = Label(frame1,text='Designation : ', font=('times new roman',15),fg='black', bg='white').place(x=10,y=200)
        ent_designation= Entry(frame1,font=('times new roman',15),textvariable=self.var_emp_designation,bg='lightyellow',fg='black')
        ent_designation.place(x=200,y=200,width=200)

        btn_qr = Button(frame1,text='Generate QR',command=self.generate,font=('times new roman',13,'bold'),bg='green',fg='white')
        btn_qr.place(x=100,y=250,width=150)

        btn_clear = Button(frame1,text='Clear',command=self.clear,font=('times new roman',13,'bold'),bg='red',fg='white')
        btn_clear.place(x=260,y=250,width=150)

        self.msg=''
        self.lbl_msg = Label(frame1,text=self.msg, font=('times new roman',20),fg='green', bg='white')
        self.lbl_msg.place(x=0,y=290,relwidth=1)



        ################### Frame 2 ###############################################
        frame2 = Frame(self.root,bd=10,relief=RIDGE,bg='white')
        frame2.place(x=600,y=80,width=250,height=350)

        self.qr_code = Label(frame2,text=' No QR \nAvailable',font=('times new roman',15),bg='gray',bd=2,relief=RIDGE)
        self.qr_code.place(x=28,y=80,width=180,height=180)


    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_department.set('')
        self.var_emp_designation.set('')

        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        

    def generate(self):
        if self.var_emp_code.get()=='' or self.var_emp_name.get()=='' or self.var_emp_department.get()=='' or self.var_emp_designation.get()=='':
            self.msg = 'All Fields are Required!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data = (f"Employee ID:{self.var_emp_code.get()}\nEmployee Name:{self.var_emp_name.get()}\nDepartment:{self.var_emp_department.get()}\nDesignation:{self.var_emp_designation.get()} ")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Employee_Or/Emp_"+str(self.var_emp_code.get())+'.png')

            ########## QR code Image Update #########
            self.im = ImageTk.PhotoImage(file="Employee_Or/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)

            ###### Updating Notification ##########
            self.msg = 'QR Generated Successfully!!'
            self.lbl_msg.config(text=self.msg,fg='green')

root=Tk()
ob = Qr_Generator(root)
root.mainloop()