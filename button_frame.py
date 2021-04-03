from tkinter import*
from tkinter import messagebox, ttk
import pymysql
class Button_Frame:
    def __init__(self,root):
        self.root = root
        self.root.title("All My GUI Softwere | Developer By VISHESH")
        self.root.geometry("1350x700+0+0")
        self.root.focus_force()
       # self.bg=PhotoImage(file="C:/vishesh/web_code/login/image6.png")
        self.bg=PhotoImage(file="login/image7.png")
        bg=Label(self.root,image=self.bg, bd=0).place(x=0, y=0, relwidth=1, relheight=1)

        text_ = Label(self.root,text="All My Project From Python GUI Apllications",font=('Algerian',40,'bold'),fg='white',bg='red').place(x=20,y=20)
        text_ = Label(self.root,text="GO All My Projects Click Here",font=('Algerian',40,'bold'),fg='white',bg='red').place(x=200,y=100)

        btn_1 = Button(self.root,text="Employee Payroll",command=self.employee_window,font=('Calibri',35,'bold'),fg='black',bg='yellow').place(x=20,y=250,width=400,height=100)

        btn_2 = Button(self.root,text="QR Generator",command=self.qr_window,font=('Calibri',35,'bold'),fg='black',bg='yellow').place(x=460,y=250,width=400,height=100)

        btn_3 = Button(self.root,text="School Management",command=self.school_window,font=('Calibri',35,'bold'),fg='black',bg='yellow').place(x=900,y=250,width=400,height=100)

        text_ = Label(self.root,text="Thankyou Visiting this side and Use Softwere",font=('Algerian',40,'bold'),fg='white',bg='red').place(x=20,y=450)
        text_ = Label(self.root,text="Developer By => VISHESH SOLANKI",font=('Algerian',40,'bold'),fg='white',bg='red').place(x=200,y=530)
         

    def employee_window(self):
        self.root.destroy()
        import employee_payroll

    def qr_window(self):
        self.root.destroy()
        import qr_generator

    def school_window(self):
        self.root.destroy()
        import school_system

root = Tk()
obj = Button_Frame(root)
root = mainloop()