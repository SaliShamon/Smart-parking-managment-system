#********************admin module**************
import sqlite3
conn=sqlite3.connect("user_authentication.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS ADMIN(
    admin_username TEXT,
    admin_password TEXT
)""")
class admin:
    def __init__(self):
        c.execute("""SELECT * FROM ADMIN""")
        if c.fetchone() is None:
         c.execute("""INSERT INTO ADMIN(admin_username,admin_password) VALUES(?,?)""",("admin","admin@123"))
        conn.commit()
        


    def admin_login(self):

        print("admin login")
        self.admin_username=input("enter your admin username:")
        self.admin_password=input("enter your admin password:")
        print("admin login")
        c.execute("""SELECT * FROM ADMIN WHERE admin_username=? AND admin_password=?""",(self.admin_username,self.admin_password))
        result=c.fetchone()
        if result is None:
          print("invalid input!try again.")
          return False
        else:
         print("login successfull")
         return True
    
        
if __name__=="__main__":
  admin_obj=admin()
  admin_obj.admin_login()
