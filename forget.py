#==================forget.py========================
# This file contains the code for the forget page
#===================================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
# create class student
class forget:
    # create constructor
    def __init__(self, root):
       self.root = root
       self.root.title("Department of CSTE")
       self.root.geometry("450x500+300+50")
       self.root.resizable(False, False)  # disable resize

       #============================all variables============================
       self.username_var=StringVar()
       self.newpassword_var=StringVar()
       self.confirm_password_var=StringVar()


      #========================title frame============================================
       title_frame = Frame(self.root, bd=3, relief=RIDGE, bg="crimson")
       title_frame.place(x=0, y=0, width=450, height=500)
       
       m_title=Label(title_frame, text="Password Modify", font=("times new roman", 30, "bold"),bg="crimson",fg='black')
       m_title.place(x=70, y=20)


       #===================================manage frame==================================

       manage_frame = Frame(self.root, bd=3, relief=RIDGE, bg="lightyellow")
       manage_frame.place(x=0, y=100, width=450, height=500)


       lable_username = Label(manage_frame, text="User Name", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_username.grid(row=3, column=0, pady=10, padx=20, sticky="w")

       txt_username = Entry(manage_frame, textvariable=self.username_var, font=("times new roman", 15, "bold"),bd=4, relief=GROOVE)
       txt_username.grid(row=3, column=1, pady=10, padx=20, sticky="w")


       lable_newpassword = Label(manage_frame, text="New Password ", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_newpassword.grid(row=4, column=0, pady=10, padx=20, sticky="w")

       txt_newpassword= Entry(manage_frame,textvariable=self.newpassword_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_newpassword.grid(row=4, column=1, pady=10, padx=20, sticky="w")

       #=========================confirm password==========================
       lable_confirmpassword = Label(manage_frame, text="Confirm Password ", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_confirmpassword.grid(row=5, column=0, pady=10, padx=20, sticky="w")

       txt_cpassword= Entry(manage_frame,textvariable=self.confirm_password_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_cpassword.grid(row=5, column=1, pady=10, padx=20, sticky="w")


       #==============================button frame==============================================

       passwordUpdate=Button(manage_frame, text=" Update ",command=self.forget, font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=8, column=1, padx=15, pady=10)
    
    #  ========== back button ===============
       backbtn=Button(manage_frame, text=" Back to Login ",command=self.back, font=("times new roman", 15, "bold"), bg="gray", fg="white").grid(row=9, column=0, padx=15, pady=10)
    def  back(self):
        root.destroy()
        import login

    def forget(self):
        username=self.username_var.get()
        newpassword=self.newpassword_var.get()
        confirmpassword=self.confirm_password_var.get()
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("select * from admin where username='%s'"%username)
        data=cur.fetchall()
        if len(data)==0:
            messagebox.showerror("Error","Invalid User Name")
        else:
            if newpassword==confirmpassword:
                cur.execute("update admin set password='%s' where username='%s'"%(newpassword,username))
                con.commit()
                messagebox.showinfo("Success","Password Updated")
                root.destroy()
                import login
            else:
                messagebox.showerror("Error","Password Not Match")
        con.close()

root = Tk()
obj = forget(root)
root.mainloop()

