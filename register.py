#==================register.py========================
# This file contains the code for the register page
#=====================================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
# create class student
class register:
    # create constructor
    def __init__(self, root):
       self.root = root
       self.root.title("Department of CSTE")
       self.root.geometry("450x500+300+50")
       self.root.resizable(False, False)  # disable resize

       #====================================all variables===========================================
       self.first_name_var = StringVar()
       self.last_name_var = StringVar()
       self.username_var=StringVar()
       self.password_var=StringVar()

      #===================================title frame================================================
       title_frame = Frame(self.root, bd=3, relief=RIDGE, bg="crimson")
       title_frame.place(x=0, y=0, width=450, height=500)
       
       m_title=Label(title_frame, text="Admin Register Form", font=("times new roman", 30, "bold"),bg="crimson",fg='black')
       m_title.place(x=25, y=20)


       #===============================manage frame==================================================

       manage_frame = Frame(self.root, bd=3, relief=RIDGE, bg="lightyellow")
       manage_frame.place(x=0, y=100, width=450, height=500)


       lable_fname = Label(manage_frame, text="First Name", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_fname.grid(row=1, column=0, pady=10, padx=20, sticky="w")

       txt_fname = Entry(manage_frame,textvariable=self.first_name_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_fname.grid(row=1, column=1, pady=10, padx=20, sticky="w")

       lable_lname = Label(manage_frame, text="Last Name", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_lname.grid(row=2, column=0, pady=10, padx=20, sticky="w")

       txt_fname = Entry(manage_frame,textvariable=self.last_name_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_fname.grid(row=2, column=1, pady=10, padx=20, sticky="w")

       lable_username = Label(manage_frame, text="User Name", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_username.grid(row=3, column=0, pady=10, padx=20, sticky="w")

       txt_username = Entry(manage_frame, textvariable=self.username_var, font=("times new roman", 15, "bold"),bd=4, relief=GROOVE)
       txt_username.grid(row=3, column=1, pady=10, padx=20, sticky="w")

       lable_password = Label(manage_frame, text="Password", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_password.grid(row=4, column=0, pady=10, padx=20, sticky="w")

       txt_password= Entry(manage_frame,textvariable=self.password_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_password.grid(row=4, column=1, pady=10, padx=20, sticky="w")


       #==========================================button frame=============================

       Applybtn=Button(manage_frame, text=" Apply ",command=self.new_admin, font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=6, column=1, padx=15, pady=10)
       backbtn=Button(manage_frame, text=" Back to Login ",command=self.back, font=("times new roman", 15, "bold"), bg="gray", fg="white").grid(row=7, column=0, padx=15, pady=10)
    def  back(self):
        root.destroy()
        import login

    def new_admin(self):
        newuser = self.username_var.get()
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("select * from admin where username='"+newuser+"'")
        rows=cur.fetchall()
        if newuser=="":
            messagebox.showerror("Error","Please enter all the fields")
        elif len(rows)==0:
                    cur.execute("insert into admin values(%s,%s,%s,%s)",(
                                                                           self.first_name_var.get(),
                                                                           self.last_name_var.get(),
                                                                           self.username_var.get(),
                                                                           self.password_var.get()))
                    con.commit()
                    self.clear()
                    messagebox.showinfo("Success","New Admin Added Successfully")
                    root.destroy()
                    import login
        else:
            messagebox.showinfo("Failed!!", "Username already exists")
            self.clear()

        
        con.close()





    def clear(self):
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.username_var.set("")
        self.password_var.set("")

        

root = Tk()
obj = register(root)
root.mainloop()

