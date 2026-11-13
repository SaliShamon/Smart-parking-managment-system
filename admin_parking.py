import sqlite3
conn=sqlite3.connect("user_authentication.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS PARKINGS(
    parking_slot TEXT PRIMARY KEY,
    status TEXT
)""")
def add_parking_slot():
    parking_slot=input("enter the parking slot you want to add:")
    c.execute("""INSERT INTO PARKINGS(parking_slot,status) VALUES(?,?)""",(parking_slot,"available"))
    conn.commit()
    print("slot added successfully")
def view_parking_slots():
    c.execute("""SELECT * FROM PARKINGS""")
    result=c.fetchall()
    if not result:
        print("no slots are available")
    else:
        print("available parking slots:")
        for i in result:
            print(i)
def view_available_slots():
    c.execute("""SELECT * FROM PARKINGS WHERE status=?""",("available",))
    result=c.fetchall()
    if not result:
        print("no slots are available")
    else:
        print("available parking slots:")
        for i in result:
            print(i)
def update_parking_slot():
    parking_slot=input("enter the parking slot you want to update:")
    new_status=input("enter the new status:")
    c.execute("""UPDATE PARKINGS SET status=? WHERE parking_slot=?""",(new_status,parking_slot))
    conn.commit()
    print("slot updated successfully")
def delete_parking_slot():
    parking_slot=input("enter the parking slot you want to delete:")
    c.execute("""DELETE FROM PARKINGS WHERE parking_slot=?""",(parking_slot,))
    conn.commit()
    print("slot deleted successfully")
def admin_menu():
 while True:
    print("1.add parking slot")
    print("2.view parking slots")
    print("3.view available slots")
    print("4.update parking slot")
    print("5.delete parking slot")
    print("6.exit")
    choice=input("enter your choice:")
    if choice=="1":
        add_parking_slot()
    elif choice=="2":
        view_parking_slots()
    elif choice=="3":
        view_available_slots()
    elif choice=="4":
        update_parking_slot()
    elif choice=="5":
        delete_parking_slot()
    elif choice=="6":
        break
    else:
        print("invalid choice!try again.")
if __name__=="__main__":
    admin_menu()