#************book slot****************

import sqlite3
conn=sqlite3.connect("user_authentication.db")
conn.execute("PRAGMA foreign_keys = ON")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS BOOKING(
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    parking_slot TEXT,
    FOREIGN KEY(parking_slot) REFERENCES PARKINGS(parking_slot))""")
def bookslot():
    user_id=input("enter your username:")
    parking_slot=input("enter thr parking slot you want to book:")
    c.execute("""SELECT * FROM PARKINGS WHERE parking_slot=? AND status=?""",(parking_slot,"available")) 
    result=c.fetchone()
    if result==None:
        print("slot is not available")
    else:
        c.execute("""INSERT INTO BOOKING(user_id,parking_slot) VALUES(?,?)""",(user_id,parking_slot))
        c.execute("""UPDATE PARKINGS SET status=? WHERE parking_slot=?""",("booked",parking_slot))
        conn.commit()
        print("slot booked successfully")
if __name__=="__main__":
 bookslot()   


