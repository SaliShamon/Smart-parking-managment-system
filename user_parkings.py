#*****viewing available parking slots********
import sqlite3
conn=sqlite3.connect("user_authentication.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS PARKINGS(
    parking_slot TEXT PRIMARY KEY,
    status TEXT
)""")

class USER_PARKINGS:
    def __init__(self):
        self.parking_slots=("A1","A2","A3","A4","A5","B1","B2","B3","B4","B5")
        for slot in self.parking_slots:
            c.execute("""INSERT OR IGNORE INTO PARKINGS (parking_slot,status) VALUES(?,?)""",(slot,"available"))
            conn.commit()

    def viewslots(self):
        print("parking_slots")
        c.execute("""SELECT * FROM PARKINGS WHERE status=?""",("available",))
        result=c.fetchall()
        if not result:
            print("no slots are free")
        else:
            print("available")
            for i in result:
                print(i[0])
if __name__=="__main__":
  obj_userparking=USER_PARKINGS()
  obj_userparking.viewslots()






            

    
