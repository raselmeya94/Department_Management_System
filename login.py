#==========================login.py============================
# This file contains the login function for the web server.
# It is called by the web server when a user attempts to login.
# It checks the username and password against the database.
# If the user is found, it returns a home page.
# If the user is not found, it returns an error message.
#================================================================


from tkinter import *
from PIL import  ImageTk
from tkinter import messagebox
import pymysql
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Department of CSTE")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        self.root.config(bg="white")
        #==============================BG Image=====================================
        self.bg_img = ImageTk.PhotoImage(file="login.png")
        self.bg_img_label = Label(self.root, image=self.bg_img)
        self.bg_img_label.place(x=0, y=0, relwidth=1, relheight=1)
        #======================welcome frame=================================
        title = Label(self.root, text="Welcome to Department of CSTE",bd=10,relief=GROOVE, font=("times new roman", 35, "bold"), bg="lightgreen", fg='red')
        title.pack(side=TOP, fill=X)

        #==============================BG Image================================
        #==============================Top=====================================
        self.top = Frame(self.root, bg="white")
        self.top.place(x=670, y=140, relwidth=0.38, relheight=0.1)
        self.top_title = Label(self.top, text="Login", font=("times new roman", 40, "bold"), bg="white", fg="Blue")
        self.top_title.place(x=0, y=0, relwidth=1, relheight=1)
        #==============================Top=====================================

        #==============================rigth========================================
        self.rigth = Frame(self.root, bg="gray")
        self.rigth.place(x=690, y=201, relwidth=0.37, relheight=0.5)
        #==============================rigth========================================
        #==============================username========================================
        self.username = Label(self.rigth, text="Username", font=("times new roman", 20, "bold"), bg="gray", fg="white")
        self.username.place(x=70, y=0)
        self.username_entry = Entry(self.rigth, font=("times new roman", 20, "bold"), bd=5, bg="white")
        self.username_entry.place(x=70, y=35)
        #==============================username========================================
        #==============================password========================================
        self.password = Label(self.rigth, text="Password", font=("times new roman", 20, "bold"), bg="gray", fg="white")
        self.password.place(x=70, y=80)
        self.password_entry = Entry(self.rigth, font=("times new roman", 20, "bold"), bd=5, bg="white")
        self.password_entry.place(x=70, y=120)
        #==============================password========================================
        #==============================login========================================
        self.login = Button(self.rigth, text="Login", font=("times new roman", 20, "bold"), bg="white", fg="black", command=self.login_verify)
        self.login.place(x=15, y=240)
        #==============================login========================================
        #==============================register========================================
        self.register = Button(self.rigth, text="Register", font=("times new roman", 20, "bold"), bg="white", fg="black", command=self.register_verify)
        self.register.place(x=300, y=240)
        #==============================register========================================
        #==============================forget========================================
        self.forget = Button(self.rigth, text="Forget Password", font=("times new roman", 15, "bold"), bg="white", fg="black", command=self.forget_verify)
        self.forget.place(x=70, y=170)
        #==============================forget========================================
    def login_verify(self):
        username1 = self.username_entry.get()
        password1 = self.password_entry.get()
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("select * from admin where username='"+username1+"' and password='"+password1+"'")
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            messagebox.showinfo("Success", "Login Successfully")
            self.clear()
            root.destroy()
            import home
    def register_verify(self):

        root.destroy()
        import register

    def forget_verify(self):
        if self.username_entry.get()!="":
            if messagebox.askyesno("Forget Password", "Do you want to reset your password"):
                root.destroy()
                import forget
        else:
            messagebox.showerror("Error", "Please enter your username")

    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)


root=Tk()
root.title("Login")
obj=Login(root)
root.mainloop()