#***********user authentication***************
import sqlite3
conn=sqlite3.connect("user_authentication.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS USERS(
    username TEXT,
    password TEXT
)""")
class userauthentication:
    def user_registration(self):
       print("user registration")
       self.username=input("enter a username:")
       self.password=input("enter a password:")
       c.execute("""INSERT INTO USERS(username,password) VALUES(?,?)""",(self.username,self.password))
       conn.commit()
       print("registration succesfull")
    def user_login(self):
        print("user login")
        self.user_name=input("enter your username:")
        self.user_password=input("enter your password:")
        c.execute("""SELECT * FROM USERS WHERE username=? AND password=?""",(self.user_name,self.user_password))
        result=c.fetchone()
        if result==None:
            print("invalid input!try again.")
            return False
        else:
            print("login successfull")
            return True
    
if __name__=="__main__":
  
  obj=userauthentication()
  obj.user_registration()
  obj.user_login()

