#Password Manager
import getpass
from openpyxl import Workbook
accounts = []
mpwd = "1234"
def save_excel():
    page_excel = Workbook()
    page = page_excel.active
    page.append(["site","username","password"])
    for i in accounts:
        page.append([i["site"],i["username"],i["password"]])
    page_excel.save("save password.xlsx")

def show():
    pass1 = getpass.getpass("Enter password...")
    for i,account in enumerate(accounts):
        if pass1 != mpwd:
            pwd = "*******"
        else:
            pwd = account["password"]
        print(f"{i+1} - sit : {account["site"]} | user : {account["username"]} | password : {pwd} ")
while True:

    print("\n1- Add account\n2- Show accounts\n3- Search\n4- Delete\n0- Exit")
    try:
        num = int(input("Enter number of options..."))
    except ValueError as ex:
        print("Please enter number...")
        num = int(input("Enter number of options..."))
    
    if num == 1 : 
        try:
            n = int(input("Enter number for adds..."))
        except ValueError:
            nn = input("Please enter a numbre...")
        for i in range(n):
            site = input("Enter site...  ")
            username = input("Enter username...  ")
            password = getpass.getpass("Enter password...")
            account = {
                "site" : site,
                "username" : username,
                "password" : password 
            }
            accounts.append(account) 
    elif num == 2:  
        show()
    elif num == 3:
        search = input("enter name of site...").lower()
        fone = False
        for i in accounts:
            if search in i["site"].lower():
                pass1 = getpass.getpass("Enter password...")
                if pass1 != mpwd:
                    pwd = "*******"
                else:
                    pwd = account["password"]
                print(f" sit : {account["site"]} | user : {account["username"]} | password : {pwd} ")
                fone = True 
        if not fone :
            print("Not found !!! ")
    elif num == 4:
        show()
        while True:
            try:
                delete = int(input("enter number options for delete...")) - 1
                accounts.pop(delete)
                break
            except ValueError:
                del_op=int(input("Please enter a number..."))
                accounts.pop(delete)
    elif num == 0:
        save_excel()
        print("good bye")
        break
    else:
        print("Options not found")
