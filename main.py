import user_authentication
import admin_module
import admin_parking
import user_parkings
import user_booking
def main_menu():
    while True:
        print("/n=====SMART PARKING MANAGMENT SYSTEM======")
        print("1.user registration")
        print("2.user login")
        print("3.admin login")
        print("4.view available parking slots")
        print("5.book parking slot")
        print("6.exit")
        choice=input("enter your choice:")
        if choice=="1":
             obj=user_authentication.userauthentication()
             obj.user_registration()
             print("user registration")
        elif  choice=="2":
             obj=user_authentication.userauthentication()
             obj.user_login()
             print("user login")
        elif choice=="3":
              obj=admin_module.admin()
              if obj.admin_login():
                   admin_parking.admin_menu()
              print("admin login")
        elif choice=="4":
             obj=user_parkings.USER_PARKINGS()
             obj.viewslots()
        elif choice=="5":
             user_booking.bookslot()
        elif choice=="6":
              print("thankyou!")
              break
        else:
             print("invalid choice!try again")
if __name__=="__main__":
     main_menu()
