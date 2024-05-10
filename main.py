from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class Signup:
    def __init__(self, root):
        self.root = root
        self.root.title("SignUp")
        self.root.geometry("925x500+300+150")
        self.root.configure(bg="white")

        self.db = sqlite3.connect('student_ms.db')
        self.c = self.db.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE,password TEXT)''')

        self.user_var = StringVar()
        self.pass_var = StringVar()
        self.rpass_var = StringVar()

        img = PhotoImage(file="signup.png")
        self.label_image = Label(root, image=img, bg="white")
        self.label_image.image = img
        self.label_image.place(x=25, y=20)

        s_frame = Frame(root, width=400, height=452, bg="white")
        s_frame.place(x=500, y=25)

        heading = Label(s_frame, text="Sign up", fg="#57a1f8", bg="white",font=("Microsoft YaHei UI Light", 30, "bold"))
        heading.place(x=110, y=30)

        def on_enter(e):
            user.delete(0, "end")

        def on_leave(e):
            users = user.get()
            if users == "":
                user.insert(0, "Username")

        user = Entry(s_frame, width=38, textvariable=self.user_var, fg="Black", border=0, bg="white", font=("Microsoft YaHei UI Light", 12))
        user.place(x=10, y=125)
        user.insert(0, "Username")
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        Frame(s_frame, width=352, height=2, bg="black").place(x=5, y=152)

        def on_enter(e):
            pas.delete(0, "end")

        def on_leave(e):
            passs = pas.get()
            if passs == "":
                pas.insert(0, "Password")

        pas = Entry(s_frame, width=38, textvariable=self.pass_var, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 12))
        pas.place(x=10, y=195)
        pas.insert(0, "Password")
        pas.bind("<FocusIn>", on_enter)
        pas.bind("<FocusOut>", on_leave)
        Frame(s_frame, width=352, height=2, bg="black").place(x=5, y=222)

        def on_enter(e):
            rpas.delete(0, "end")

        def on_leave(e):
            rpasss = rpas.get()
            if rpasss == "":
                rpas.insert(0, "Conform Password")

        rpas = Entry(s_frame, width=38, textvariable=self.rpass_var, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 12))
        rpas.place(x=10, y=265)
        rpas.insert(0, "Conform Password")
        rpas.bind("<FocusIn>", on_enter)
        rpas.bind("<FocusOut>", on_leave)
        Frame(s_frame, width=352, height=2, bg="black").place(x=5, y=292)

        Button(s_frame, width=39, command=self.add, pady=7, text="Sign up", bg="#57a1f8", fg="white", border=0).place(x=40, y=329)
        label = Label(s_frame, text="I have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 10))
        label.place(x=100, y=370)

        signin = Button(s_frame, command=self.signup, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#57a1f8")
        signin.place(x=215, y=373)

    def add(self):
        try:
            username = self.user_var.get()
            password = self.pass_var.get()
            confirm_password = self.rpass_var.get()

            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match!")
                return

            self.c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
            self.db.commit()
            messagebox.showinfo("Success", "User inserted successfully!")
            self.root.destroy()
            login_window = Tk()
            Login(login_window)
            login_window.mainloop()

        except Exception as e:
            print("Error occurred:", e)

    def signup(self):
        self.root.destroy()
        login_window = Tk()
        Login(login_window)
        login_window.mainloop()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("925x500+300+150")
        self.root.configure(bg="white")
        self.db = sqlite3.connect('student_ms.db')
        self.c = self.db.cursor()

        def signin():
            username = user.get()
            password = pas.get()
            self.c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
            users = self.c.fetchone()
            if users:
                self.root.destroy()
                Student()
            else:
                messagebox.showerror("Error", "Invalid Username or Password")

        img = PhotoImage(file="login.png")
        self.label_image = Label(root, image=img, bg="white")
        self.label_image.image = img
        self.label_image.place(x=25, y=20)

        l_frame = Frame(root, width=400, height=452, bg="white")
        l_frame.place(x=500, y=25)

        heading = Label(l_frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 30, "bold"))
        heading.place(x=140, y=50)

        def on_enter(e):
            user.delete(0, "end")

        def on_leave(e):
            users = user.get()
            if users == "":
                user.insert(0, "Username")

        user = Entry(l_frame, width=38, fg="Black", border=0, bg="white", font=("Microsoft YaHei UI Light", 12))
        user.place(x=30, y=145)
        user.insert(0, "Username")
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        Frame(l_frame, width=352, height=2, bg="black").place(x=25, y=172)

        def on_enter(e):
            pas.delete(0, "end")

        def on_leave(e):
            passs = pas.get()
            if passs == "":
                pas.insert(0, "Password")

        pas = Entry(l_frame, width=38, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 12))
        pas.place(x=30, y=215)
        pas.insert(0, "Password")
        pas.bind("<FocusIn>", on_enter)
        pas.bind("<FocusOut>", on_leave)
        Frame(l_frame, width=352, height=2, bg="black").place(x=25, y=242)

        Button(l_frame, width=39, pady=7, command=signin, text="Sign in", bg="#57a1f8", fg="white", border=0).place(x=60, y=279)
        label = Label(l_frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 10))
        label.place(x=100, y=320)

        signup = Button(l_frame, width=6, command=self.signup, text="Sign Up", border=0, bg="white", cursor="hand2", fg="#57a1f8")
        signup.place(x=255, y=323)

    def signup(self):
        self.root.destroy()
        signup_window = Tk()
        Signup(signup_window)
        signup_window.mainloop()

class Student:
    def __init__(self):
        self.root = Tk()
        self.db = sqlite3.connect('student_ms.db')
        self.c = self.db.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS student (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                roll TEXT,
                                name TEXT,
                                email TEXT,
                                dep TEXT,
                                gpa TEXT,
                                contact TEXT,
                                dob TEXT,
                                city TEXT)''')

        self.root.title("Student Management System")
        self.root.geometry("1350x700+75+50")
        self.root.configure(bg="white")

        title = Label(self.root, text="Student Management System", font=("times new roman", 40, "bold"), bg="#57a1f8", fg="white")
        title.pack(side=TOP, fill=X)

        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.dep_var = StringVar()
        self.gpa_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.city_var = StringVar()
        self.search_var = StringVar()


        Manage_Frame = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Manage_Frame.place(x=20,y=100,width=450,height=570)

        m_title = Label(Manage_Frame, text="Manage Student", font=("times new roman", 30, "bold"),fg="black",bg="white")
        m_title.grid()

        r_lab = Label(Manage_Frame, text="Roll No", font=("times new roman", 12, "bold"),fg="black",bg="white")
        r_lab.place(x=30,y=75)
        roll_no = Entry(Manage_Frame, textvariable=self.roll_var, width=30, fg="black", border=0, font=("times new roman", 12))
        roll_no.place(x=180,y=75)
        Frame(Manage_Frame,width=250,height=2,bg="black").place(x=175,y=97)

        n_lab = Label(Manage_Frame, text="Name", font=("times new roman", 12, "bold"), fg="black", bg="white")
        n_lab.place(x=30, y=115)
        name = Entry(Manage_Frame, width=30, textvariable=self.name_var, fg="black", border=0, font=("times new roman", 12))
        name.place(x=180, y=115)
        Frame(Manage_Frame, width=250, height=2, bg="black").place(x=175, y=137)

        e_lab = Label(Manage_Frame, text="Email", font=("times new roman", 12, "bold"), fg="black", bg="white")
        e_lab.place(x=30, y=155)
        email = Entry(Manage_Frame, textvariable=self.email_var, width=30, fg="black", border=0, font=("times new roman", 12))
        email.place(x=180, y=155)
        Frame(Manage_Frame, width=250, height=2, bg="black").place(x=175, y=177)

        d_lab = Label(Manage_Frame, text="Department", font=("times new roman", 12, "bold"), fg="black", bg="white")
        d_lab.place(x=30, y=195)
        dep = Entry(Manage_Frame, textvariable=self.dep_var, width=30, fg="black", border=0, font=("times new roman", 12))
        dep.place(x=180, y=195)
        Frame(Manage_Frame, width=250, height=2, bg="black").place(x=175, y=217)

        g_lab = Label(Manage_Frame, text="Current GPA", font=("times new roman", 12, "bold"), fg="black", bg="white")
        g_lab.place(x=30, y=235)
        gpa = Entry(Manage_Frame, width=30, textvariable=self.gpa_var, fg="black", border=0, font=("times new roman", 12))
        gpa.place(x=180, y=235)
        Frame(Manage_Frame, width=250, height=2, bg="black").place(x=175, y=257)

        c_lab = Label(Manage_Frame, text="Contact Number", font=("times new roman", 12, "bold"), fg="black", bg="white")
        c_lab.place(x=30, y=275)
        contact = Entry(Manage_Frame, width=30, textvariable=self.contact_var, fg="black", border=0, font=("times new roman", 12))
        contact.place(x=180, y=275)
        Frame(Manage_Frame, width=250, height=2, bg="black").place(x=175, y=297)

        d_lab = Label(Manage_Frame, text="Date of Birth", font=("times new roman", 12, "bold"), fg="black", bg="white")
        d_lab.place(x=30, y=315)
        dob = Entry(Manage_Frame, width=30, textvariable=self.dob_var, fg="black", border=0, font=("times new roman", 12))
        dob.place(x=180, y=315)
        Frame(Manage_Frame, width=250, height=2, bg="black").place(x=175, y=337)

        ce_lab = Label(Manage_Frame, text="City", font=("times new roman", 12, "bold"), fg="black", bg="white")
        ce_lab.place(x=30, y=355)
        city = Entry(Manage_Frame, width=30, textvariable=self.city_var, fg="black", border=0, font=("times new roman", 12))
        city.place(x=180, y=355)
        Frame(Manage_Frame, width=250, height=2, bg="black").place(x=175, y=377)

        Button(Manage_Frame, width=25, command=self.add_student, pady=7, text="Add", bg="#57a1f8", fg="white", border=0, font=("times new roman", 10, "bold")).place(x=30, y=430)
        Button(Manage_Frame, width=25, command=self.update_student, pady=7, text="Update", bg="#57a1f8", fg="white", border=0,font=("times new roman", 10,"bold")).place(x=230, y=430)
        Button(Manage_Frame, width=25, command=self.delete_student, pady=7, text="Delete", bg="#57a1f8", fg="white", border=0,font=("times new roman", 10,"bold")).place(x=30, y=480)
        Button(Manage_Frame, width=25, command=self.clear, pady=7, text="Clear", bg="#57a1f8", fg="white", border=0,font=("times new roman", 10,"bold")).place(x=230, y=480)

        Detail_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Detail_Frame.place(x=500, y=100, width=830, height=570)

        d_title = Label(Detail_Frame, font = ("times new roman",30,"bold"), bg = "#57a1f8",fg = "white")
        d_title.pack(side=TOP,fill=X)

        dr_lab = Label(Detail_Frame, text="Roll No", font=("times new roman", 12, "bold"), fg="white", bg="#57a1f8")
        dr_lab.place(x=410, y=14)
        droll_no = Entry(Detail_Frame,width=26,textvariable=self.search_var,bg = "#57a1f8",fg="white",border=0,font=("times new roman", 12,"bold"))
        droll_no.place(x=475,y=14)
        Frame(Detail_Frame,width=217,height=2,bg="black").place(x=470,y=36)

        Button(Detail_Frame, width=15, command=self.search_student, pady=7, text="Search", bg="white", fg="black", border=0,font=("times new roman", 10, "bold")).place(x=700, y=8)

        Table_Frame = Frame(Detail_Frame, bd=3, relief=RIDGE, bg="white")
        Table_Frame.place(y=50, width=825, height=515)

        scoral_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scoral_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.s_table = ttk.Treeview(Table_Frame,columns=("id","roll","name","email","dep","gpa","contact","dob","city"), xscrollcommand=scoral_x.set,yscrollcommand=scoral_y.set)
        scoral_x.pack(side=BOTTOM,fill=X)
        scoral_y.pack(side=RIGHT,fill=Y)
        scoral_x.config(command=self.s_table.xview)
        scoral_y.config(command=self.s_table.yview)
        self.s_table.heading("id", text="Number")
        self.s_table.heading("roll", text="Roll No.")
        self.s_table.heading("name", text="Name")
        self.s_table.heading("email", text="Email")
        self.s_table.heading("dep", text="Department")
        self.s_table.heading("gpa", text="GPA")
        self.s_table.heading("contact", text="Contact No.")
        self.s_table.heading("dob", text="Date of Birth")
        self.s_table.heading("city", text="City")

        for col in self.s_table["columns"]:
            self.s_table.column(col, anchor="center")

        self.s_table["show"] = "headings"
        self.s_table.pack(fill=BOTH,expand=1)
        self.s_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        self.root.mainloop()

    def add_student(self):
        try:
            self.c.execute("INSERT INTO student (roll, name, email, dep, gpa, contact, dob, city) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
                self.roll_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.dep_var.get(),
                self.gpa_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.city_var.get()
            ))
            self.db.commit()
            messagebox.showinfo("Success","Data inserted successfully!")
            self.fetch_data()
        except Exception as e:
            print("Error occurred:", e)

    def clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.dep_var.set("")
        self.gpa_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.city_var.set("")

    def update_student(self):
        try:
            self.c.execute(
                "UPDATE student SET name=?, email=?, dep=?, gpa=?, contact=?, dob=?, city=? WHERE roll=?",
                (
                    self.name_var.get(),
                    self.email_var.get(),
                    self.dep_var.get(),
                    self.gpa_var.get(),
                    self.contact_var.get(),
                    self.dob_var.get(),
                    self.city_var.get(),
                    self.roll_var.get()
                )
            )
            self.db.commit()
            messagebox.showinfo("Success","Data updated successfully!")
            self.fetch_data()
            self.clear()
        except Exception as e:
            print("Error occurred:", e)

    def delete_student(self):
        try:
            roll_no = self.roll_var.get()
            self.c.execute("DELETE FROM student WHERE roll=?", (roll_no,))
            self.db.commit()
            messagebox.showinfo("Success","Data deleted successfully!")
            self.fetch_data()
            self.clear()
        except Exception as e:
            print("Error occurred:", e)

    def search_student(self):
        try:
            roll = str(self.search_var.get())
            self.c.execute("SELECT * FROM student WHERE roll=?", (roll,))
            rows = self.c.fetchall()
            if len(rows) != 0:
                self.s_table.delete(*self.s_table.get_children())
                for row in rows:
                    self.s_table.insert('', 'end', values=row)
            else:
                print("No matching student found.")
        except Exception as e:
            print("Error occurred:", e)

    def fetch_data(self):
        try:
            self.c.execute("SELECT * FROM student")
            rows = self.c.fetchall()
            if len(rows) != 0:
                self.s_table.delete(*self.s_table.get_children())
                for row in rows:
                    self.s_table.insert('', 'end', values=row)
        except Exception as e:
            print("Error occurred:", e)

    def get_cursor(self,ev):
        cursor_row = self.s_table.focus()
        contents = self.s_table.item(cursor_row)
        row = contents['values']
        self.roll_var.set(row[1])
        self.name_var.set(row[2])
        self.email_var.set(row[3])
        self.dep_var.set(row[4])
        self.gpa_var.set(row[5])
        self.contact_var.set(row[6])
        self.dob_var.set(row[7])
        self.city_var.set(row[8])

root = Tk()
ob = Login(root)
root.mainloop()
