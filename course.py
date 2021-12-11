#==================course.py========================
# This file contains the code for the course page
#===================================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
# create class student
class course:
    # create constructor
    def __init__(self, root):
       self.root = root
       self.root.title("Department of CSTE")
       self.root.geometry("1350x700+0+0")

       #===============================all variables=====================================
       self.course_id_var = StringVar()
       self.course_name_var = StringVar()
       self.course_year_var=StringVar()
       self.course_teacher_id_var=StringVar()
       self.search_by = StringVar()
       self.search_txt = StringVar()


       title = Label(self.root, text="Courses Management",bd=10,relief=GROOVE, font=("times new roman", 40, "bold"), bg="lightgreen", fg='red')
       title.pack(side=TOP, fill=X)
       homeBtn=Button(self.root,text="Back Home",command=self.back_home,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
       homeBtn.place(x=10,y=10)
       #============================manage frame=====================================================
       manage_frame = Frame(self.root, bd=3, relief=RIDGE, bg="lightyellow")
       manage_frame.place(x=15, y=100, width=450, height=600)
       
       m_title=Label(manage_frame, text="Add New Course", font=("times new roman", 30, "bold"), bg="gray",fg='white')
       m_title.grid(row=0, columnspan=2, pady=15)

       lbl_id = Label(manage_frame, text="Course ID", font=("times new roman", 15, "bold"), bg="lightyellow")
       lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

       txt_id = Entry(manage_frame,textvariable=self.course_id_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

       lable_coursename = Label(manage_frame, text="Course Name", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_coursename.grid(row=2, column=0, pady=10, padx=20, sticky="w")

       txt_coursename = Entry(manage_frame,textvariable=self.course_name_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_coursename.grid(row=2, column=1, pady=10, padx=20, sticky="w")


       lable_course_year = Label(manage_frame, text="Course Year", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_course_year.grid(row=4, column=0, pady=10, padx=15, sticky="w")

       txt_course_year = Entry(manage_frame, textvariable=self.course_year_var,font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_course_year.grid(row=4, column=1, pady=10, padx=20, sticky="w")

       lable_course_teacher_id = Label(manage_frame, text="Course teacher ID", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_course_teacher_id.grid(row=5, column=0, pady=10, padx=15, sticky="w")

       txt_course_teacher_id = Entry(manage_frame,textvariable=self.course_teacher_id_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_course_teacher_id.grid(row=5, column=1, pady=10, padx=20, sticky="w")


       #================================================button frame================================================-
       button_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="crimson")
       button_frame.place(x=10, y=525, width=420)

       Addbtn=Button(button_frame, text=" Add ",command=self.add_course, font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=0, padx=15, pady=10)
       Updatebtn=Button(button_frame, text="Update", command=self.update_data, font=("times new roman", 15, "bold"), bg="#ff00ff", fg="white").grid(row=0, column=1, padx=15, pady=10)
       Deletebtn=Button(button_frame, text="Delete", command=self.delete_data, font=("times new roman", 15, "bold"), bg="#116548", fg="white").grid(row=0, column=2, padx=15, pady=10)
       Clearbtn=Button(button_frame, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="red", fg="white").grid(row=0, column=3, padx=15, pady=10)



       #=============================details frame===========================================
       detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_frame.place(x=500, y=100, width=840, height=490)


       lblSearch = Label(detail_frame, text="Search By", font=("times new roman", 15, "bold"), bg="gray")
       lblSearch.grid(row=0, column=0, pady=10, padx=20, sticky="w")
       # search combobox
       combo_search= ttk.Combobox(detail_frame,textvariable=self.search_by, width=10,font=("times new roman", 13, "bold"),state='readonly')
       combo_search['values']=("course_id", "course_name", "course_year", "course_teacher_id")
       combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

       txt_search = Entry(detail_frame,textvariable=self.search_txt, width=15, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

       searchbtn=Button(detail_frame,command=self.search_data, text="Search",width=10, font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=3, padx=15, pady=10)
       showallbtn=Button(detail_frame, text="Show All",command=self.fetch_data, width=10,font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=4, padx=15, pady=10)
     
        #====================================details frame table===============================================
        # table frame
       table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
       table_frame.place(x=10, y=70, width=810, height=400)
        # details developer
       dev_section = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
       dev_section.place(x=500, y=595, width=840, height=100)
       # developer frame
       detail_dev = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_dev.place(x=503, y=600, width=350, height=90)
       lbl_author = Label(detail_dev, text="Developed By", font=("Helvetica",30, "bold"), fg="red",bg='gray')
       lbl_author.grid(row=0, column=0, pady=10, padx=20, sticky="w")

       detail_author= Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_author.place(x=860, y=600, width=470, height=90)
       lbl_author = Label(detail_author, text="Md. Rasel Meya\nDepartment of CSTE\nNoakhali Science & Technology University.", font=("times new roman", 15, "bold"),bg="gray")
       lbl_author.grid(row=0, column=1, pady=10, padx=20, sticky="w")
       lbl_author.pack()


       #==============================student table=====================================================
       scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = Scrollbar(table_frame, orient=VERTICAL)
       self.course_table = ttk.Treeview(table_frame, columns=("course_id", "course_name", "course_year","course_teacher_id"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)
       scroll_x.config(command=self.course_table.xview)
       scroll_y.config(command=self.course_table.yview)
       self.course_table.heading("course_id", text="Course ID")
       self.course_table.heading("course_name", text="Course Name")
       self.course_table.heading("course_year",text="Course Year")
       self.course_table.heading("course_teacher_id", text="Course teacher ID")
       self.course_table.column("course_id", width=100)
       self.course_table.column("course_name", width=100)
       self.course_table.column("course_year", width=100)
       self.course_table.column("course_teacher_id", width=100)
       self.course_table['show']='headings'
       self.course_table.pack(fill=BOTH, expand=1)
       self.course_table.bind("<ButtonRelease-1>", self.get_cursor)
       self.fetch_data() 
    #======================add course Info.=========================================
    def add_course(self):
        if self.course_id_var.get()!="":
            #==============teacher available check==============
            teacher =  self.course_teacher_id_var.get()
            con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
            cur=con.cursor()
            cur.execute("select * from teacher where teacher_id='"+teacher+"'")
            rows=cur.fetchall()
            if len(rows)!=0:
                con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
                cur=con.cursor()
                cur.execute("insert into courses values(%s,%s,%s,%s)",(self.course_id_var.get(),
                                                                                self.course_name_var.get(),
                                                                                self.course_year_var.get(),
                                                                                self.course_teacher_id_var.get()))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success", "Course Added Successfully")
            else:
                messagebox.showerror("Error", "Teacher ID Not Avaiable!")
        else:
            messagebox.showerror("Error", "Please Enter Course Details")
    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("select * from courses")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)
                con.commit()
        
        con.close()
    def clear(self):
        self.course_id_var.set("")
        self.course_name_var.set("")
        self.course_year_var.set("")
        self.course_teacher_id_var.set("")
    def get_cursor(self,ev):
        cursor_row=self.course_table.focus()
        contents=self.course_table.item(cursor_row)
        row=contents['values']
        self.course_id_var.set(row[0])
        self.course_name_var.set(row[1])
        self.course_year_var.set(row[2])
        self.course_teacher_id_var.set(row[3])

    #==============================update student details=====================================
    def update_data(self):
            #==============teacher available check==============
            teacher =  self.course_teacher_id_var.get()
            con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
            cur=con.cursor()
            cur.execute("select * from teacher where teacher_id='"+teacher+"'")
            rows=cur.fetchall()
            if len(rows)!=0:
                con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
                cur=con.cursor()
                cur.execute("update courses set course_name=%s,course_year=%s,course_teacher_id=%s where course_id=%s",(self.course_name_var.get(),
                                                                                                                                    self.course_year_var.get(),
                                                                                                                                    self.course_teacher_id_var.get(),
                                                                                                                                    self.course_id_var.get()
                                                                                                                                    ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success", "Course Udated Successfully")
            else:
                messagebox.showerror("Error", "Teacher ID Not Avaiable!")


    #===================================delete student details=================================
    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("delete from courses where course_id=%s",self.course_id_var.get())
        # confirmation messagebox
        ask_del=messagebox.askyesno("Department Management System","Do you want to delete this course info?")
        if ask_del>0:
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
        else:
            return


    #================================search_box=========================
    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
        cur=con.cursor()
        cur.execute("select * from courses where "+self.search_by.get()+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)
                con.commit()
        else:
            messagebox.showerror("Department Management System","No Course Data Found")

        con.close()
    def back_home(self):
        root.destroy()
        import home;




root = Tk()
obj = course(root)
root.mainloop()

