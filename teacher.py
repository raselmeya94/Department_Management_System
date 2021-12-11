#==================teacher.py========================
# This file contains the code for the teacher page
#===================================================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
# create class student
class teacher:
    # create constructor
    def __init__(self, root):
       self.root = root
       self.root.title("Department of CSTE")
       self.root.geometry("1350x700+0+0")

       #==================================all variables================================================
       self.teacher_id_var = StringVar()
       self.teacher_name_var = StringVar()
       self.teacher_email_var=StringVar()
       self.teacher_contact_var=StringVar()
       self.search_by = StringVar()
       self.search_txt = StringVar()


       title = Label(self.root, text="Teacher Management",bd=10,relief=GROOVE, font=("times new roman", 40, "bold"), bg="lightgreen", fg='red')
       title.pack(side=TOP, fill=X)
       homeBtn=Button(self.root,text="Back Home",command=self.back_home,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
       homeBtn.place(x=10,y=10)
       # ====================================manage frame====================================================
       manage_frame = Frame(self.root, bd=3, relief=RIDGE, bg="lightyellow")
       manage_frame.place(x=15, y=100, width=450, height=600)
       
       m_title=Label(manage_frame, text="Add New Teacher", font=("times new roman", 30, "bold"), bg="gray",fg='white')
       m_title.grid(row=0, columnspan=2, pady=15)

       lbl_teacherid = Label(manage_frame, text="Teacher ID", font=("times new roman", 15, "bold"), bg="lightyellow")
       lbl_teacherid.grid(row=1, column=0, pady=10, padx=20, sticky="w")

       txt_teacherid = Entry(manage_frame,textvariable=self.teacher_id_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_teacherid.grid(row=1, column=1, pady=10, padx=20, sticky="w")

       lable_teachername = Label(manage_frame, text="Teacher Name", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_teachername.grid(row=2, column=0, pady=10, padx=20, sticky="w")

       txt_teachername = Entry(manage_frame,textvariable=self.teacher_name_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_teachername.grid(row=2, column=1, pady=10, padx=20, sticky="w")


       lable_teacheremail = Label(manage_frame, text="Teacher Email", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_teacheremail.grid(row=4, column=0, pady=10, padx=15, sticky="w")

       txt_teacheremail = Entry(manage_frame, textvariable=self.teacher_email_var,font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_teacheremail.grid(row=4, column=1, pady=10, padx=20, sticky="w")

       lable_teachercontact = Label(manage_frame, text="Teacher Contact", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_teachercontact.grid(row=5, column=0, pady=10, padx=15, sticky="w")

       txt_teachercontact = Entry(manage_frame,textvariable=self.teacher_contact_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_teachercontact.grid(row=5, column=1, pady=10, padx=20, sticky="w")


       # ===================================button frame=================================================
       button_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="crimson")
       button_frame.place(x=10, y=525, width=420)

       Addbtn=Button(button_frame, text=" Add ",command=self.add_teacher, font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=0, padx=15, pady=10)
       Updatebtn=Button(button_frame, text="Update", command=self.update_data, font=("times new roman", 15, "bold"), bg="#ff00ff", fg="white").grid(row=0, column=1, padx=15, pady=10)
       Deletebtn=Button(button_frame, text="Delete", command=self.delete_data, font=("times new roman", 15, "bold"), bg="#116548", fg="white").grid(row=0, column=2, padx=15, pady=10)
       Clearbtn=Button(button_frame, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="red", fg="white").grid(row=0, column=3, padx=15, pady=10)



       #=====================================details frame====================================================
       detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_frame.place(x=500, y=100, width=840, height=490)


       lblSearch = Label(detail_frame, text="Search By", font=("times new roman", 15, "bold"), bg="gray")
       lblSearch.grid(row=0, column=0, pady=10, padx=20, sticky="w")
       #============================search combobox===========================================================
       combo_search= ttk.Combobox(detail_frame,textvariable=self.search_by, width=10,font=("times new roman", 13, "bold"),state='readonly')
       combo_search['values']=("teacher_id", "teacher_name", "teacher_email", "teacher_contact")
       combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")
       #==========================text box=====================================================================
       txt_search = Entry(detail_frame,textvariable=self.search_txt, width=15, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        #===========================search button=======================================================================
       searchbtn=Button(detail_frame,command=self.search_data, text="Search",width=10, font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=3, padx=15, pady=10)
       showallbtn=Button(detail_frame, text="Show All",command=self.fetch_data, width=10,font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=4, padx=15, pady=10)
     
        #======================================================details frame table=====================================================
        # =============================table frame======================================
       table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
       table_frame.place(x=10, y=70, width=810, height=400)
        #=================details developer=================================================
       dev_section = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
       dev_section.place(x=500, y=595, width=840, height=100)
       #=======================developer frame=================================
       detail_dev = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_dev.place(x=503, y=600, width=350, height=90)
       lbl_author = Label(detail_dev, text="Developed By", font=("Helvetica",30, "bold"), fg="red",bg='gray')
       lbl_author.grid(row=0, column=0, pady=10, padx=20, sticky="w")

       detail_author= Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_author.place(x=860, y=600, width=470, height=90)
       lbl_author = Label(detail_author, text="Md. Rasel Meya\nDepartment of CSTE\nNoakhali Science & Technology University.", font=("times new roman", 15, "bold"),bg="gray")
       lbl_author.grid(row=0, column=1, pady=10, padx=20, sticky="w")
       lbl_author.pack()


       #=========================teacher table=============================
       scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = Scrollbar(table_frame, orient=VERTICAL)
       self.teacher_table = ttk.Treeview(table_frame, columns=("teacher_id", "teacher_name", "teacher_email","teacher_contact"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)
       scroll_x.config(command=self.teacher_table.xview)
       scroll_y.config(command=self.teacher_table.yview)
       self.teacher_table.heading("teacher_id", text="Teacher ID")
       self.teacher_table.heading("teacher_name", text="Teacher Name")
       self.teacher_table.heading("teacher_email",text="Teacher Email")
       self.teacher_table.heading("teacher_contact", text="Teacher Contact No.")
       self.teacher_table.column("teacher_id", width=100)
       self.teacher_table.column("teacher_name", width=100)
       self.teacher_table.column("teacher_email", width=100)
       self.teacher_table.column("teacher_contact", width=100)
       self.teacher_table['show']='headings'
       self.teacher_table.pack(fill=BOTH, expand=1)
       self.teacher_table.bind("<ButtonRelease-1>", self.get_cursor)
       self.fetch_data() 
    #=========================add teacher details==============================
    def add_teacher(self):
        if self.teacher_id_var.get()!="":

            con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
            cur=con.cursor()
            cur.execute("insert into teacher values(%s,%s,%s,%s)",(self.teacher_id_var.get(),
                                                                            self.teacher_name_var.get(),
                                                                            self.teacher_email_var.get(),
                                                                            self.teacher_contact_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","New teacher added")
        else:
            messagebox.showerror("Error","All fields are required!!")
    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("select * from teacher")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for row in rows:
                self.teacher_table.insert('',END,values=row)
                con.commit()
        
        con.close()
    def clear(self):
        self.teacher_id_var.set("")
        self.teacher_name_var.set("")
        self.teacher_email_var.set("")
        self.teacher_contact_var.set("")
    def get_cursor(self,ev):
        cursor_row=self.teacher_table.focus()
        contents=self.teacher_table.item(cursor_row)
        row=contents['values']
        self.teacher_id_var.set(row[0])
        self.teacher_name_var.set(row[1])
        self.teacher_email_var.set(row[2])
        self.teacher_contact_var.set(row[3])

    #=========================update teacher details==============================
    def update_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("update teacher set teacher_name=%s,teacher_gmail=%s,teacher_contact=%s where teacher_id=%s",(self.teacher_name_var.get(),
                                                                                                                            self.teacher_email_var.get(),
                                                                                                                            self.teacher_contact_var.get(),
                                                                                                                            self.teacher_id_var.get()
                                                                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Teacher Update Successfully")


    #=========================delete teacher details==============================
    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("delete from teacher where teacher_id=%s",self.teacher_id_var.get())
        # confirmation messagebox
        ask_del=messagebox.askyesno("Department Management System","Do you want to delete this course info?")
        if ask_del>0:
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Teacher Information Successfully Delete")
        else:
            return


    #==================search box query=========================================
    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("select * from teacher where "+self.search_by.get()+" LIKE '%"+(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for row in rows:
                self.teacher_table.insert('',END,values=row)
                con.commit()
        else:
            messagebox.showerror("Department Management System","No teacher Data Found")

        con.close()

    def back_home(self):
        root.destroy()
        import home;





root = Tk()
obj = teacher(root)
root.mainloop()

