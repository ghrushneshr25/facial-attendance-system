query = "INSERT INTO studentdetails (`RollNo`, `name`, `email id`, `year` , `branch`, `password`, `div`) VALUES ( %s, %s , %s, %s, %s , %s, %s)"
                record = (rollNo, name, email, year, branch, password, div)
                # print(query, record)
                cursor.execute(query, record)

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