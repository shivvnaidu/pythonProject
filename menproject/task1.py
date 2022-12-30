from tkinter import *
from tkinter import messagebox
import mysql.connector

class LoginPage:
    def __init__(self):
        pass
    def my_details(self,id):
        conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl2')
        cur1 = conn.cursor()
        try:
            val = int(id)
            try:
                cur1.execute("SELECT * FROM login WHERE id=" + id)
                result = cur1.fetchone()
                search.set(result)
            except:
                search.set("Database as error")
        except:
            search.set("Check given input")


    def search(self):
        global window3
        window3 = Toplevel(window)
        window3.title("Search Page")
        window3.geometry("600x300")
        global search
        l1 = Label(window3, text='Enter ID to search', width=45)
        l1.grid(row=1, column=1)
        t1 = Text(window3, height=1, width=5, bg='#57a1f8')
        t1.grid(row=1, column=2)
        b1 = Button(window3, text='Show Details', width=15, bg='#57a1f8', command=lambda: self.my_details(t1.get('1.0', END)))
        b1.grid(row=1, column=4)
        search = StringVar()
        l2 = Label(window3, textvariable=search, width=30, fg='#57a1f8')
        l2.grid(row=3, column=1, columnspan=2)
        search.set("")
        window3.mainloop()


    def sining(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl2')
        query = "select id from login where username =%s and password=%s"
        value = (username1.get(), password1.get())
        cur = conn.cursor(prepared=True)
        cur.execute(query, value)
        result = cur.fetchone()
        if result != None:
            messagebox.showinfo('message', 'user already exist')
        else:
            q1 = "insert into login(username,password) values(?,?)"
            value = (username1.get(), password1.get())
            # cur=conn.cursor()
            cur.execute(q1, value)
            conn.commit()
            messagebox.showinfo('message', 'new user added successfully')


    def signin(self):
        global window2
        window2 = Toplevel(window)
        window2.geometry("400x400")
        window2.title("sign-in")
        global username1
        global password1
        global renter

        username1 = StringVar()
        password1 = StringVar()
        renter = StringVar()
        Label(window2, text="enter username").grid(row=0)
        Entry(window2, textvariable=username1)
        Label(window2, text="Password").grid(row=1)
        Entry(window2, textvariable=password1)
        Label(window2, text="Re-enter Password").grid(row=2)
        Entry(window2, textvariable=renter)
        b = Button(window2, text="signup", command=self.sining).grid(row=4)
        e1 = Entry(window2, textvariable=username1)
        e2 = Entry(window2, textvariable=password1)
        e3 = Entry(window2, textvariable=renter)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        window2.mainloop()


    def logging(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl2')
        query = "select id from login where username =%s and password=%s"
        val = (username.get(), password.get())
        cur = conn.cursor(prepared=True)
        cur.execute(query, val)
        result = cur.fetchone()
        if result != None:
            messagebox.showinfo('message', 'login success')
        else:
            messagebox.showinfo('message', 'invalid ')


    def login(self):
        global window1
        window1 = Toplevel(window)
        window1.geometry("400x400")
        window1.title("log in page")
        global username
        global password
        username = StringVar()
        password = StringVar()
        Label(window1, text="enter username").grid(row=0)
        Entry(window1, textvariable=username)
        Label(window1, text="Password").grid(row=1)
        Entry(window1, textvariable=password)

        b = Button(window1, text="login", command=self.logging).grid(row=3)
        e1 = Entry(window1, textvariable=username)
        e2 = Entry(window1, textvariable=password)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        window1.mainloop()


    def mains(self):
        global window
        window = Tk()
        window.geometry("400x400")
        window.title("HCL EMP SYSTEM")
        menubar = Menu(window)
        menubar.add_command(label="Login", command=self.login)
        menubar.add_command(label="New User", command=self.signin)
        menubar.add_command(label="Search", command=self.search)
        window.config(menu=menubar)
        window.mainloop()
if __name__=='__main__':
    obj=LoginPage()
    obj.mains()
