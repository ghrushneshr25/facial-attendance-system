import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import Button
import mysql.connector
from mysql.connector import errorcode
from tkinter import *


class demo:

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abcd1234",
            database="attendance"
        )
        cursor = mydb.cursor()

    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)

    register = tk.Tk()
    register.title("Registration")
    register.geometry("300x200")
    register.configure(background='#F0F8FF')

    rollNoLabel = Label(register, text="Roll No",
                        bg='#F0F8FF', font=('courier', 10, 'normal'))
    nameLabel = Label(register, text="Name", bg='#F0F8FF',
                      font=('courier', 10, 'normal'))
    emailLabel = Label(register, text="Email", bg='#F0F8FF',
                       font=('courier', 10, 'normal'))
    yearLabel = Label(register, text="Year", bg='#F0F8FF',
                      font=('courier', 10, 'normal'))
    branchLabel = Label(register, text="Branch", bg='#F0F8FF',
                        font=('courier', 10, 'normal'))
    passwordLabel = Label(register, text="Password",
                          bg='#F0F8FF', font=('courier', 10, 'normal'))

    enterRollNo = Entry(register, width=10)
    enterName = Entry(register, width=40)
    enterEmail = Entry(register)
    enterYear = Entry(register)
    enterBranch = Entry(register)
    enterPassword = Entry(register)

    rollNoLabel.place(x=10, y=30)
    nameLabel.place(x=10, y=50)
    emailLabel.place(x=10, y=70)
    yearLabel.place(x=10, y=90)
    branchLabel.place(x=10, y=110)
    passwordLabel.place(x=10, y=130)

    enterRollNo.place(x=100, y=30)
    enterName.place(x=100, y=50)
    enterEmail.place(x=100, y=70)
    enterYear.place(x=100, y=90)
    enterBranch.place(x=100, y=110)
    enterPassword.place(x=100, y=130)

    register.mainloop()
    mydb.close()


demo()
