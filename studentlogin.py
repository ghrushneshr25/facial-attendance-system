from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import time
import random

k = 0


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        # =====Login Frame============
        self.Frame_login = Frame(self.root, bg="white")
        self.Frame_login.place(x=125, y=200, height=340, width=400)

        title = Label(self.Frame_login, text="Login Here", font=(
            "Impact", 35, "bold"), fg="#5465ff", bg="white")
        title.place(x=25, y=30)

        desc = Label(self.Frame_login, text="Student Login", font=(
            "Goudy old style", 15, "bold"), fg="#788bff", bg="white")
        desc.place(x=25, y=100)

        label_user = Label(self.Frame_login, text="Username", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        label_user.place(x=25, y=140)

        self.txt_user = Entry(self.Frame_login, font=(
            "times new roman", 15), bg="lightgray")

        self.txt_user.place(x=25, y=170, width=350, height=35)

        label_pass = Label(self.Frame_login, text="Password", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        label_pass.place(x=25, y=210)

        self.txt_pass = Entry(self.Frame_login, font=(
            "times new roman", 15), bg="lightgray", show='*')

        self.txt_pass.place(x=25, y=240, width=350, height=35)

        self.login_btn = Button(self.root, text="Login", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.login)

        self.login_btn.place(x=180, y=525)

        self.register_btn = Button(self.root, text="Register", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.registerButton)

        self.register_btn.place(x=330, y=525)
        k = 1

    def checkCredentials(self, rollno, passcode):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abcd1234",
                database="attendance"
            )
            cursor = mydb.cursor()
            sqlQuery = "SELECT PASSWORD FROM STUDENTDETAILS WHERE ROLLNO = '"+rollno+"'"
            cursor.execute(sqlQuery)
            record = cursor.fetchone()
            if (record[0] == passcode):
                return True
            else:
                return False
        except Exception as e:
            return False
        return False

    def login(self):

        username = self.txt_user.get()
        password = self.txt_pass.get()
        if username != "" and password != "":

            logIn = self.checkCredentials(username, password)

            if(logIn == True):
                self.Frame_login.destroy()
                self.login_btn.destroy()
                self.register_btn.destroy()
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="abcd1234",
                    database="attendance"
                )
                cursor = mydb.cursor()
                sql = "Select role from studentdetails where ROLLNO='"+username+"'"
                cursor.execute(sql)
                result = cursor.fetchone()
                cursor.close()
                mydb.close()
                if(result[0] == 'Faculty'):
                    loggedin = Loggedin_Faculty(root, username)

                else:
                    loggedin = Loggedin(root, username)
            else:
                messagebox.showerror(
                    "Error", "Invalid Credentials", parent=self.root)

        else:
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)

    def registerButton(self):
        self.Frame_login.destroy()
        self.register_btn.destroy()
        self.login_btn.destroy()
        registerHere = Register(root)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")

        self.backButton = Button(self.root, text="Back", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.backpress)
        self.backButton.place(x=0, y=0)

        # --- REGISTER FRAME----
        self.Frame_register = Frame(self.root, bg="white")
        self.Frame_register.place(x=225, y=25, height=740, width=400)

        title = Label(self.Frame_register, text="Register", font=(
            "Impact", 35, "bold"), fg="#5465ff", bg="white")
        title.place(x=20, y=30)

        desc = Label(self.Frame_register, text="Student Register", font=(
            "Goudy old style", 15, "bold"), fg="#788bff", bg="white")
        desc.place(x=20, y=100)

        labelRollNo = Label(self.Frame_register, text="Roll No", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelRollNo.place(x=20, y=140)

        self.txtRollNo = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray")

        self.txtRollNo.place(x=20, y=170, width=160, height=35)

        labelDiv = Label(self.Frame_register, text="Div", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelDiv.place(x=220, y=140)

        self.txtDiv = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray")

        self.txtDiv.place(x=220, y=170, width=160, height=35)

        labelName = Label(self.Frame_register, text="Name", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelName.place(x=20, y=210)

        self.txtName = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray")

        self.txtName.place(x=20, y=240, width=360, height=35)

        labelEmailId = Label(self.Frame_register, text="Email ID", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelEmailId.place(x=20, y=280)

        self.txtEmailId = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray")

        self.txtEmailId.place(x=20, y=310, width=360, height=35)

        "-------------------------------------------------------"

        labelYear = Label(self.Frame_register, text="Year", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelYear.place(x=20, y=350)

        self.currentYear = StringVar(None)
        self.currentYear.set("FE")

        self.radioYearFE = Radiobutton(self.Frame_register, text="FE", variable=self.currentYear, value="FE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearFE.place(x=20, y=380, width=90, height=35)

        self.radioYearSE = Radiobutton(self.Frame_register, text="SE", variable=self.currentYear, value="SE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearSE.place(x=110, y=380, width=90, height=35)

        self.radioYearTE = Radiobutton(self.Frame_register, text="TE", variable=self.currentYear, value="TE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearTE.place(x=200, y=380, width=90, height=35)

        self.radioYearBE = Radiobutton(self.Frame_register, text="BE", variable=self.currentYear, value="BE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearBE.place(x=290, y=380, width=90, height=35)

        "------------------------------------------------------"

        labelBranch = Label(self.Frame_register, text="Branch", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelBranch.place(x=20, y=420)

        self.selectedBranch = StringVar()
        self.selectedBranch.set("COMPUTER ENGINEERING")

        self.radioBranchCOMPS = Radiobutton(self.Frame_register, text="Computer", variable=self.selectedBranch, value="COMPUTER ENGINEERING", font=(
            "times new roman", 15), bg="lightgray", justify=LEFT)
        self.radioBranchCOMPS.place(x=20, y=450, width=360, height=35)

        self.radioBranchIT = Radiobutton(self.Frame_register, text="Information Technology", variable=self.selectedBranch, value="INFORMATION TECHNOLOGY", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchIT.place(x=20, y=480, width=360, height=35)

        self.radioBranchEXTC = Radiobutton(self.Frame_register, text="Electronics and Telecommunication", variable=self.selectedBranch, value="ELECTRONICS AND TELECOMMUNICATION ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchEXTC.place(x=20, y=510, width=360, height=35)

        self.radioBranchETRX = Radiobutton(self.Frame_register, text="Electronics", variable=self.selectedBranch, value="ELECTRONICS ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchETRX.place(x=20, y=540, width=360, height=35)

        self.radioBranchINSTRU = Radiobutton(self.Frame_register, text="Instrumentation", variable=self.selectedBranch, value="INSTRUMENTATION ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchINSTRU.place(x=20, y=570, width=360, height=35)

        "--------------------------------------------------------"
        labelPassword = Label(self.Frame_register, text="Password", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelPassword.place(x=20, y=610)

        self.txtPassword = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray", show='*')

        self.txtPassword.place(x=20, y=640, width=360, height=35)

        self.registerButton = Button(self.Frame_register, text="Register", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.registerNow)
        self.registerButton.place(x=250, y=690)

    def registerNow(self):

        rollNo = self.txtRollNo.get()
        div = self.txtDiv.get()
        year = self.currentYear.get()
        branch = self.selectedBranch.get()
        name = self.txtName.get()
        email = self.txtEmailId.get()
        password = self.txtPassword.get()

        if rollNo == "" or div == "" or name == "" or email == "" or branch == "" or password == "" or year == "":
            messagebox.showerror(
                "Error", "Invalid Input", parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="abcd1234",
                    database="attendance"
                )
                cursor = mydb.cursor()
                query = "INSERT INTO studentdetails (`RollNo`, `name`, `email id`, `year` , `branch`, `password`, `div`) VALUES ( %s, %s , %s, %s, %s , %s, %s)"
                record = (rollNo, name, email, year, branch, password, div)
                # print(query, record)
                cursor.execute(query, record)
                mydb.commit()
                messagebox.showinfo(message="Successful registration!")
                self.backpress()
            except mysql.connector.Error as e:
                if e.errorcode == 1062:
                    messagebox.showerror(message="User already registered")
                else:
                    messagebox.showerror(message="Error")
                self.backpress()
                mydb.rollback()
            finally:
                if mydb is not None:
                    cursor.close()
                    mydb.close()

    def backpress(self):
        self.Frame_register.destroy()
        self.backButton.destroy()
        logindisplay = Login(root)


class Loggedin:
    def __init__(self, root, roll_no):
        self.roll_no = roll_no
        self.root = root
        self.root.title("Logged In")
        self.backButton = Button(self.root, text="Back", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.backpress)
        self.backButton.place(x=0, y=0)

        self.create_session_frame = Frame(self.root, bg="white")
        self.create_session_frame.place(x=125, y=200, height=340, width=400)
        title = Label(self.create_session_frame, text="Session Details", font=(
            "Impact", 35, "bold"), fg="#5465ff", bg="white")
        title.place(x=25, y=30)
        label_user = Label(self.create_session_frame, text="Enter Session Key:", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        label_user.place(x=25, y=140)

        self.s_key = Entry(self.create_session_frame, font=(
            "times new roman", 15), bg="lightgray")

        self.s_key.place(x=25, y=170, width=350, height=35)

        self.session_start = Button(self.create_session_frame, text="Start Session", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.session_start)

        self.session_start.place(x=150, y=225)
        label_end = Label(self.create_session_frame, text="Press and Q to end Session", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        label_end.place(x=25, y=280)

        self.photoFrame = Frame(self.root, bg="white")
        self.photoFrame.place(x=600, y=200, height=340, width=400)

        self.uploadImageButton = Button(self.photoFrame, text="Upload Image",
                                        bg="#d77337", fg="white", font=("times new roman", 15), width=10, command=self.uploadImage)
        self.uploadImageButton.place(x=100, y=300)

    def uploadImage(self):
        print("Uploading")
        return

    def backpress(self):
        self.backButton.destroy()
        self.photoFrame.destroy()
        self.create_session_frame.destroy()
        logindisplay = Login(root)

    def session_start(self):
        path = "testimages"
        images = []
        className = []

        myList = os.listdir(path)
    # print(myList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            className.append(os.path.splitext(cl)[0])

        encodeListKnown = self.findEncodings(images)
        print(len(encodeListKnown))

        print("--VIDEO CAMERA ABOUT TO START--")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        print("-----VIDEO CAMERA STARTED------")

        totalFrames, countFrame = 0, 0

        starttime = time.time()

        while True:
            success, img = cap.read()

            imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

            if time.time() - starttime > 10:
                totalFrames = totalFrames + 1
                faceFrame = face_recognition.face_locations(imgSmall)
                encodeFrame = face_recognition.face_encodings(
                    imgSmall, faceFrame)
                starttime = time.time()

                for encodeFace, faceLoc in zip(encodeFrame, faceFrame):
                    matches = face_recognition.compare_faces(
                        encodeListKnown, encodeFace)
                    faceDistance = face_recognition.face_distance(
                        encodeListKnown, encodeFace)
                    matchIndex = np.argmin(faceDistance)

                    if matches[matchIndex]:
                        countFrame = countFrame + 1
                        rollNo = className[matchIndex].upper()
            cv2.imshow("Webcam", img)
            cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        self.markAttendance(
            self.roll_no, totalFrames, countFrame)
    # print(className)

    def findEncodings(self, images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)

        return encodeList

    def markAttendance(self, rollno, totalFrames, countFrame):
        if(totalFrames > 5):
            if(((countFrame/totalFrames)*100) > 90):
                with open('attendance.csv', 'r+') as f:
                    myDataList = f.readlines()
                    rollNoList = []
                    for line in myDataList:
                        entry = line.split(",")
                        rollNoList.append(entry[0])
                    if rollno not in rollNoList:
                        now = datetime.now()
                        dtString = now.strftime("%H:%M:%S")
                        f.writelines(f'\n{rollno},{dtString}')
        return


class Loggedin_Faculty:

    def __init__(self, root, username):
        self.username = username
        self.root = root
        self.root.title("Logged In")
        self.backButton = Button(self.root, text="Back", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.backpress)
        self.backButton.place(x=0, y=0)

        self.create_session_frame = Frame(self.root, bg="white")
        self.create_session_frame.place(x=125, y=100, height=600, width=400)

        title = Label(self.create_session_frame, text="Create Session", font=(
            "Impact", 30, "bold"), fg="#5465ff", bg="white")
        title.place(x=20, y=20)

        labelDiv = Label(self.create_session_frame, text="Div", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelDiv.place(x=20, y=70)

        self.txtDiv = Entry(self.create_session_frame, font=(
            "times new roman", 15), bg="lightgray")

        self.txtDiv.place(x=20, y=100, width=160, height=35)

        labelYear = Label(self.create_session_frame, text="Year", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelYear.place(x=20, y=140)

        self.currentYear = StringVar(None)
        self.currentYear.set("FE")

        self.radioYearFE = Radiobutton(self.create_session_frame, text="FE", variable=self.currentYear, value="FE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearFE.place(x=20, y=180, width=90, height=35)

        self.radioYearSE = Radiobutton(self.create_session_frame, text="SE", variable=self.currentYear, value="SE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearSE.place(x=110, y=180, width=90, height=35)

        self.radioYearTE = Radiobutton(self.create_session_frame, text="TE", variable=self.currentYear, value="TE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearTE.place(x=200, y=180, width=90, height=35)

        self.radioYearBE = Radiobutton(self.create_session_frame, text="BE", variable=self.currentYear, value="BE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearBE.place(x=290, y=180, width=90, height=35)

        "------------------------------------------------------"

        labelBranch = Label(self.create_session_frame, text="Branch", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelBranch.place(x=20, y=220)

        self.selectedBranch = StringVar()
        self.selectedBranch.set("COMPUTER ENGINEERING")

        self.radioBranchCOMPS = Radiobutton(self.create_session_frame, text="Computer", variable=self.selectedBranch, value="COMPUTER ENGINEERING", font=(
            "times new roman", 15), bg="lightgray", justify=LEFT)
        self.radioBranchCOMPS.place(x=20, y=250, width=360, height=35)

        self.radioBranchIT = Radiobutton(self.create_session_frame, text="Information Technology", variable=self.selectedBranch, value="INFORMATION TECHNOLOGY", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchIT.place(x=20, y=285, width=360, height=35)

        self.radioBranchEXTC = Radiobutton(self.create_session_frame, text="Electronics and Telecommunication", variable=self.selectedBranch, value="ELECTRONICS AND TELECOMMUNICATION ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchEXTC.place(x=20, y=320, width=360, height=35)

        self.radioBranchETRX = Radiobutton(self.create_session_frame, text="Electronics", variable=self.selectedBranch, value="ELECTRONICS ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchETRX.place(x=20, y=355, width=360, height=35)

        self.radioBranchINSTRU = Radiobutton(self.create_session_frame, text="Instrumentation", variable=self.selectedBranch, value="INSTRUMENTATION ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchINSTRU.place(x=20, y=390, width=360, height=35)

        "--------------------------------------------------------"

        self.generate_session = Button(self.create_session_frame, text="Generate Session Key", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=32, command=self.createTable)
        self.generate_session.place(x=20, y=430)

        "---------------------------------------------------------"

        self.sessionEntry = StringVar()

        self.key = Entry(self.create_session_frame, textvariable=self.sessionEntry, font=(
            "Impact", 20))
        self.key.place(x=20, y=480)

        self.startSessionButton = Button(self.create_session_frame, text="Start Session", bg="#d77337", fg="white", font=(
            "times new roman", 10), width=20, command=self.startsession)
        self.startSessionButton.place(x=20, y=540)

        self.endSessionButton = Button(self.create_session_frame, text="End Session", bg="#d77337", fg="white", font=(
            "times new roman", 10), width=20, command=self.endsession)
        self.endSessionButton.place(x=230, y=540)

    def startsession(self):
        sessionKey = self.key.get()
        print(sessionKey)
        if sessionKey == "":
            messagebox.showerror(
                "Error", "Invalid Input", parent=self.root)
            return
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abcd1234",
                database="attendance"
            )

            cursor = mydb.cursor()

            sql = "SELECT `BRANCH`, `YEAR`, `DIV` FROM sessiontables where sessionid = '"+sessionKey+"';"
            cursor.execute(sql)
            record = cursor.fetchone()
            print(record)

            cursor.close()
            cursor = mydb.cursor()

            sql = "SELECT `ROLLNO`, `NAME` FROM studentdetails WHERE `DIV`=%s AND `YEAR`=%s AND `BRANCH`=%s AND `ROLE`='student';"
            param = (record[2], record[1], record[0])
            cursor.execute(sql, param)
            studentrecords = cursor.fetchall()
            loopcursor = mydb.cursor()
            insertsql = "INSERT INTO `"+sessionKey + \
                "` (`ROLLNO`, `NAME`) VALUES(%s , %s);"
            loopcursor.executemany(insertsql, studentrecords)

            timecursor = mydb.cursor()
            timesql = "UPDATE sessiontables SET `STARTTIME` = NOW() WHERE sessionid = '" + \
                sessionKey+"';"
            timecursor.execute(timesql)
            mydb.commit()
            cursor.close()
            loopcursor.close()
            timecursor.close()

        except mysql.connector.Error as e:
            print(e)
            mydb.rollback()

        finally:
            if mydb is not None:
                mydb.close()
        return

    def endsession(self):
        sessionKey = self.key.get()
        print(sessionKey)
        if sessionKey == "":
            messagebox.showerror(
                "Error", "Invalid Input", parent=self.root)
            return
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abcd1234",
                database="attendance"
            )
            timecursor = mydb.cursor()
            timesql = "UPDATE sessiontables SET `ENDTIME` = NOW() WHERE sessionid = '" + \
                sessionKey+"';"
            timecursor.execute(timesql)
            mydb.commit()

        except mysql.connector.Error as e:
            print(e)
            mydb.rollback()

        finally:
            if mydb is not None:
                timecursor.close()
                mydb.close()

        return

    def createTable(self):

        div = self.txtDiv.get()
        year = self.currentYear.get()
        branch = self.selectedBranch.get()

        if div == "" or year == "" or branch == "":
            messagebox.showerror(
                "Error", "Invalid Inputs", parent=self.root)
            return

        sessionKey = "".join(random.choice(
            '1Q2W3E4R5T6Y7U8I9O0PLKJHGFDSAZXVBNM') for i in range(16))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abcd1234",
                database="attendance"
            )
            FKEYCONSTRAINT = sessionKey+"constraint"
            tablesql = "CREATE TABLE " + sessionKey + \
                " (`ROLLNO` VARCHAR(8) NOT NULL, `ATTENDANCESTATUS` VARCHAR(2) NOT NULL DEFAULT 'A', `NAME` VARCHAR(100) NOT NULL, PRIMARY KEY (`ROLLNO`), CONSTRAINT `" + \
                FKEYCONSTRAINT + \
                "` FOREIGN KEY (`ROLLNO`) REFERENCES `studentdetails` (`ROLLNO`) ON DELETE NO ACTION ON UPDATE NO ACTION);"
            record2 = (sessionKey)
            print("Stage 2 initiated")
            cursor1 = mydb.cursor()
            cursor1.execute(tablesql)
            cursor1.close()
            print("stage 2 cleared")

            cursor = mydb.cursor()
            sql = "INSERT INTO SESSIONTABLES (`SESSIONID`, `YEAR`, `DIV`, `CREATETIME`, `BRANCH`, `FACULTYID`) VALUES (%s , %s , %s , NOW(), %s, %s);"
            record = (sessionKey, year, div, branch, self.username)
            cursor.execute(sql, record)
            cursor.close()
            mydb.commit()
            print("stage 1 clear")

            self.sessionEntry.set(sessionKey)

        except mysql.connector.Error as e:
            print(e)
            messagebox.showerror(
                "Error", "Error Try Again", parent=self.root)
            mydb.rollback()
        finally:
            if mydb is not None:
                mydb.close()

        # self.insertintable(sessionKey, div, year, branch)

        return

    def insertintable(self, sessionKey, div, year, branch):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abcd1234",
                database="attendance"
            )

            insertsql = "INSERT INTO 'attendance'.'%s' (`ROLLNO`, `NAME`) SELECT `ROLLNO`, `NAME` FROM `STUDENTDETAILS` WHERE `DIV` = '%s' AND `YEAR` = '%s' AND `BRANCH` ='`%s';"
            record3 = (sessionKey, div, year, branch)
            print("Stage 3 initiated")
            cursor = mydb.cursor()
            cursor.execute(insertsql, record3)
            print("stage 3 cleared")
            mydb.commit()
        except mysql.connector.Error as e:
            print(e)
            mydb.rollback()
        finally:
            if mydb is not None:
                cursor.close()
                mydb.close()
        return

    def backpress(self):
        self.backButton.destroy()
        self.create_session_frame.destroy()
        logindisplay = Login(root)


root = Tk()
width = 1280
height = 800
root.geometry("%dx%d" % (width, height))
bg = PhotoImage(file="studentattendance.png")
bg_image = Label(root, image=bg).place(
    x=0, y=0, relwidth=1, relheight=1)
root.resizable(False, False)
login = Login(root)
root.mainloop()
