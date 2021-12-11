#==================register.py========================
# This file contains the code for the register page
# Author: Md. Rasel Meya
# Department of computer science and telecommunication engineering,
# University of Noakhali Science and Technology
# created on: October 2021

#=====================================================


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from typing import ValuesView
import pymysql
# create class Home
class Home:
    # create constructor
    def __init__(self, home):
        self.home = home
        self.home.title("Department of CSTE")
        self.home.geometry("1350x750+0+0")
        self.home.config(bg="cadet blue")

        #=====================================all the variables====================

        self.search_by1 = StringVar()
        self.search_txt1 = StringVar()
        self.search_by2 = StringVar()
        self.search_txt2 = StringVar()

        #================create a frame for the home page==================================

        self.Tops = Frame(self.home,bd=14,width=1350,height=100, relief="raise")
        self.Tops.pack(side=TOP, fill=X)
        self.teacher = Frame(self.home, bd=14, relief="raise")
        self.teacher.place(x=0, y=128, width=250, height=194)
        self.student = Frame(self.home, bd=14, relief="raise")
        self.student.place(x=0, y=322, width=250, height=192)
        self.course = Frame(self.home, bd=14, relief="raise")
        self.course.place(x=0, y=514, width=250, height=192)
        self.info = Frame(self.home, bd=14, relief="raise")
        self.info.place(x=250, y=128, width=1100, height=100)
        self.detail_frame = Frame(self.home, bd=14, relief="raise",bg='gray')
        self.detail_frame.place(x=250, y=228, width=1100, height=480)
        self.info2 = Frame(self.info,bd=14, relief="raise",bg='green')
        self.info2.place(x=1, y=1, width=1070, height=70)

        #================create a label for the details frame=======================================

        self.lbl_title = Label(self.detail_frame, font=('times new roman', 50, 'bold'), text="Information Desk", bd=10,bg='gray')
        self.lbl_title.place(x=280, y=120, width=600, height=150)

        #================create a label for the home page=========================================

        self.lblinfo = Label(self.Tops, font=('times new roman', 50, 'bold',), text="\tDepartment of CSTE", fg="crimson", bd=10, anchor='w')
        self.lblinfo.grid(row=0, column=0)
        self.lblinfo = Label(self.teacher, font=('times new roman', 15, 'bold'), text="Manage\nTeacher Information", fg="Steel Blue", bd=10, anchor='w')  
        self.lblinfo.grid(row=0, column=0)
        self.lblinfo = Label(self.student, font=('times new roman', 15, 'bold'), text="Manage\nStudent Information", fg="Steel Blue", bd=10, anchor='w')
        self.lblinfo.grid(row=0, column=0)
        self.lblinfo = Label(self.course, font=('times new roman', 15, 'bold'), text="Manage\nCourse Information", fg="Steel Blue", bd=10, anchor='w')
        self.lblinfo.grid(row=0, column=0)

        #====================create search box for the home page=====================================

        self.lblinfo=Label(self.info2, font=('times new roman', 20, 'bold'), text="\t\t\tTypes of Information",bg='green', fg="white", anchor='w')
        self.lblinfo.grid(row=0, column=1)
        # search combobox table




        def show_selected_item(event):
            #==============teacher table show selected item============================================
            if self.combo.get() == 'Teachers':
                detail_frameT = Frame(self.detail_frame, bd=14, relief="raise",bg='red')
                detail_frameT.place(x=1, y=1, width=1070, height=450)
                scroll_x = Scrollbar(detail_frameT , orient=HORIZONTAL)
                scroll_y = Scrollbar(detail_frameT, orient=VERTICAL)
                teacher_table = ttk.Treeview(detail_frameT, columns=("teacher_id", "teacher_name", "teacher_email","teacher_contact"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_x.config(command=teacher_table.xview)
                scroll_y.config(command=teacher_table.yview)
                teacher_table.heading("teacher_id", text="Teacher ID")
                teacher_table.heading("teacher_name", text="Teacher Name")
                teacher_table.heading("teacher_email",text="Teacher Email")
                teacher_table.heading("teacher_contact", text="Teacher Contact No.")
                teacher_table.column("teacher_id", width=100)
                teacher_table.column("teacher_name", width=100)
                teacher_table.column("teacher_email", width=100)
                teacher_table.column("teacher_contact", width=100)
                teacher_table['show']='headings'
                teacher_table.pack(fill=BOTH, expand=1)
                con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
                cur=con.cursor()
                cur.execute("select * from teacher")
                rows=cur.fetchall()
                if len(rows)!=0:
                    teacher_table.delete(*teacher_table.get_children())
                    for row in rows:
                        teacher_table.insert('',END,values=row)
                con.commit()
                con.close()

            #==============student table show selected item============================================

            elif self.combo.get() == 'Students':
                detail_frameS = Frame(self.detail_frame, bd=14, relief="raise",bg='red')
                detail_frameS.place(x=1, y=1, width=1070, height=450)
                scroll_x = Scrollbar(detail_frameS, orient=HORIZONTAL)
                scroll_y = Scrollbar(detail_frameS, orient=VERTICAL)
                student_table = ttk.Treeview(detail_frameS, columns=("student_id", "student_name", "student_gender", "student_session", "current_year","student_email", "student_contact", "student_address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_x.config(command=student_table.xview)
                scroll_y.config(command=student_table.yview)
                student_table.heading("student_id", text="ID")
                student_table.heading("student_name", text="Name")
                student_table.heading("student_gender",text="Gender")
                student_table.heading("student_session", text="Session")
                student_table.heading("current_year", text="Current Year")
                student_table.heading("student_email", text="Email")
                student_table.heading("student_contact", text="Contact No.")
                student_table.heading("student_address", text="Address")
                student_table.column("student_id", width=100)
                student_table.column("student_name", width=100)
                student_table.column("student_gender", width=100)
                student_table.column("student_session", width=100)
                student_table.column("current_year", width=100)
                student_table.column("student_email", width=100)
                student_table.column("student_contact", width=100)
                student_table.column("student_address", width=100)
                student_table['show']='headings'
                student_table.pack(fill=BOTH, expand=1)
                con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
                cur=con.cursor()
                cur.execute("select * from student")
                rows=cur.fetchall()
                if len(rows)!=0:
                    student_table.delete(*student_table.get_children())
                    for row in rows:
                        student_table.insert('',END,values=row)
                con.commit()
                con.close()

            #==============course table show selected item============================================

            elif self.combo.get() == 'Courses':
                detail_frameC = Frame(self.detail_frame, bd=14, relief="raise",bg='red')
                detail_frameC.place(x=1, y=1, width=1070, height=450)
                scroll_x = Scrollbar(detail_frameC, orient=HORIZONTAL)
                scroll_y = Scrollbar(detail_frameC, orient=VERTICAL)
                course_table = ttk.Treeview(detail_frameC, columns=("course_id", "course_name", "course_year","course_teacher_id"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_x.config(command=course_table.xview)
                scroll_y.config(command=course_table.yview)
                course_table.heading("course_id", text="Course ID")
                course_table.heading("course_name", text="Course Name")
                course_table.heading("course_year",text="Course Year")
                course_table.heading("course_teacher_id", text="Course teacher ID")
                course_table.column("course_id", width=100)
                course_table.column("course_name", width=100)
                course_table.column("course_year", width=100)
                course_table.column("course_teacher_id", width=100)
                course_table['show']='headings'
                course_table.pack(fill=BOTH, expand=1)
                con=pymysql.connect(host="localhost", user="root", password="", database="department_of_cste")
                cur=con.cursor()
                cur.execute("select * from courses")
                rows=cur.fetchall()
                if len(rows)!=0:
                    course_table.delete(*course_table.get_children())
                    for row in rows:
                        course_table.insert('',END,values=row)
                con.commit()
                con.close()

            # create a combobox
        self.combo = ttk.Combobox(self.info2)
        self.combo['values'] = ('Teachers', 'Students', 'Courses')
        self.combo.grid(row=0, column=4, pady=10, padx=20, sticky="w")
        self.combo.bind('<<ComboboxSelected>>', show_selected_item)




        #===================================create a button for the home page========================================

        self.btnteacher = Button(self.teacher, padx=10, pady=10,  bd=4, fg="black", font=('arial', 16, 'bold'), width=10, text="Teacher", bg="Steel Blue",command=self.teacher_login)
        self.btnteacher.grid(row=1, column=0)
        self.btnstudent = Button(self.student,  padx=10, pady=10,  bd=4, fg="black", font=('arial', 16, 'bold'), width=10, text="Student", bg="Steel Blue",command=self.student_login)
        self.btnstudent.grid(row=1, column=0)
        self.btncourse = Button(self.course, padx=10, pady=10,  bd=4, fg="black", font=('arial', 16, 'bold'), width=10, text="Course", bg="Steel Blue",command=self.course_login)
        self.btncourse.grid(row=1, column=0)
 
    #=====================================create a function for the home page================================
    def teacher_login(self):
        home.destroy()
        import teacher
    #=========================create a function for the home page==============================
    def student_login(self):
        home.destroy()
        import student

    #================create a function for the home page====================
    def course_login(self):
        home.destroy()
        import course




        






home=Tk()
obj=Home(home)
home.mainloop()