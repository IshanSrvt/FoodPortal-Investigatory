import mysql.connector as pro
d=pro.connect(host="localhost",user="root",password="admin",database="food")
e=d.cursor()
 # ADDING FOOD OPTION FOR ADMIN
def add_food():

    d=pro.connect(host="localhost",user="root",password="admin",database="food")
    e=d.cursor()
    ser=int(input("Enter the Food ID:"))
    fi=input("Enter the Food name:")
    fp=int(input("Enter the Price of Food:"))
    ft=input("Enter the Food Type:")
    e.execute("insert into item values({},'{}',{},'{}')".format(ser,fi,fp,ft))
    print("NEW FOOD ADDED SUCCESSFULLY")
    d.commit()
 # UPDATING FOOD & PRICE OPTION FOR ADMIN
def update_food(): 

    d=pro.connect(host="localhost",user="root",password="admin",database="food")
    e=d.cursor()
    print("1. update food name")
    print("2. update food price")
    us=int(input("Enter your choice :"))
    if us==1:
        fnid=int(input("Enter the Food ID whose foodname you want to update :"))
        fna=input("Enter the updated Food Name: ")
        e.execute("update Item set Food_Item='{}' where S_no={}".format(fna,fnid))
        print("UPDATED SUCCESSFULLY")
        d.commit()
    elif us==2:
        fnic=int(input("Enter the Food ID whose food price you want to update :"))
        fnf=input("Enter the updated Food Price: ")
        e.execute("update Item set Prices={} whereS_no={}".format(fnf,fnic))
        print("UPDATED SUCCESSFULLY")
        d.commit()
        print("You have been Redirected to the Admin page")
        ad_login()
 # DELETING FOOD OPTION FOR ADMIN

def delete_food():

    d=pro.connect(host="localhost",user="root",password="admin",database="food")
    e=d.cursor()
    fidd=int(input("Enter the Food ID you want to delete:"))
    e.execute("delete from item where S_no={}".format(fidd))
    print("YOU HAVE DELETED A FOOD ITEM SUCCESSFULLY")
    d.commit()
 # VIEWING ORDER HISTORY OPTION FOR ADMIN
def view_orders():

    d=pro.connect(host="localhost",user="root",password="admin",database="food")
    e=d.cursor()
    fgg=("select * from orders")
    print("Details of all orders are:")
    e.execute(fgg)
    rtt=e.fetchall()
    for i in rtt:

        print("*****************************************************")
        print("Food name:",i[0])
        print("Food price:",i[1])
        print("Total price:",i[2])
        print("Phone NO:",i[3])
        print("Address:",i[4])

        print("******************************************************")
 # LOGIN OPTION FOR ADMIN
def ad_login():
    while 1:
        print("1. Add food")
        print("2. Update food")
        print("3. Delete food")
        print("4. View orders")
        print("5. Logout")
        ask=int(input("Enter your Choice: "))
        if ask==1:
            add_food()
        elif ask==2:
            update_food()
        elif ask==3:
            delete_food()
        elif ask==4:
            view_orders()
        elif ask==5:
            return
 # PASSWORD FOR ADMIN TO LOGIN
def ad_panel():
    pas=input("Enter Password :")
    if pas=='Zomato':
        print("Access granted")
        ad_login()
    else:
        print("Wrong Password")
        print("You have been REdirected to the Main Page")
    admin()
    # FOOD ITEMS TO SHOW CUSTOMER

def show_menu():
    e.execute("select * from item")
    w=e.fetchall()
    print("-------------MENU FOR TODAY---------------")
    for i in w:
        print("Food No.",i[0],"Food Name:",i[1],"-- Price:",i[2],"--Food type:",i[3] )
        d.commit()
        ui=input("Do you want to order food:")
        if ui=="Yes" or ui=="yes":
            F_order()
        else:
            print("Thank you")
            print("You have been Redirected to the Main Page")
        return
 # TO PLACE ORDER OF FOOD ITEM
def F_order():
    io=int(input("Enter the food item no. you want to order:"))
    QTY=int(input("Enter QTY of food:"))
    phn=int(input("Enter your Phone NO:"))
    ADR=input("Enter your Address:")
    fi=("select * from item where S_no={}".format(io))
    e.execute(fi)
    fi=e.fetchall()
    iname=fi[0][1]
    iprice=fi[0][2]
    oprice=iprice*QTY
    ins="insert into orders(O_name,I_price,O_price,P_no,ADR)values('{}',{},{},{},'{}')".format(iname,iprice,oprice,phn,ADR)
    print("********BILL********")
    print("Address:",ADR)
    print("Phone NO:",phn)
    print("Food name:",iname)
    print('Food price:',iprice)
    print("QTY of food:",QTY)
    print('Total price:',oprice)
    print("********************")
    print("Thanks for ordering food")
    print("Your order has been confirmed")
    print("You have been Redirected to the MAIN PAGE")
    e.execute(ins)
    d.commit()
 # VIEWING YOUR FOOD ORDER HISTORY
def F_View():
    yno=int(input("Enter your phone NO:"))
    a=("select * from orders where P_no={}").format(yno)
    e.execute(a)
    rt=e.fetchall()
    if len(rt)>0:
        for i in rt:
            print("Your recent orders are:")
            print("**********YOUR ORDER DETAILS ARE SHOWN BELOW**********")
            print("Food name:",i[0])
            print("Food price:",i[1])
            print("Total price:",i[2])
            print("Phone NO:",i[3])
            print("Address:",i[4])
    else:
        print("YOU HAVE NOT PLACED ANY ORDER")
        d.commit()
    # CANCELING YOUR FOOD ORDER 
def F_Cancel():
    cor=int(input("Enter your phone NO:"))
    dele=("delete from orders where P_no={}").format(cor)
    e.execute(dele)
    print("Your order has been cancelled SUCCESSFULLY")
    print("You have been Redirected to the MAIN PAGE")
    d.commit()
 # FEEDBACK OPTION FOR CUSTOMER
def F_feedb():
    fdb=int(input("Enter your Phone NO:"))
    print("Give us Feedback--")
    fdc=input(" ")
    fdp="insert into Feed values P_no,F_back={},'{}'".format(fdb,fdc)
    print("THANKS FOR YOUR FEEDBACK")
    print("You have been Redirected to MAIN PAGE")
    d.commit()
 # MAIN MENU FOR CUSTOMER
def main_menu():
 while True:
    print("----------------------WELCOME TO FOOD PORTAL----------------------")
    print("1. Main Menu")
    print("2. Place your Orders")
    print("3. View order")
    print("4. Cancel your Order")
    print("5. Feedback")
    print("6. Exit")
    a=int(input("Enter the Service you want:"))
    if a==1:
        show_menu()
    elif a==2:
        F_order()
    elif a==3:
        F_View()
    elif a==4:
        F_Cancel()
    elif a==5:
        F_feedb()
    elif a==6:
        break
 # HOME PAGE 
def admin():
    while True:
        print("**********************************************")
        print("WELCOME TO FOOD PORTAL")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. EXIT")
        op=int(input("Enter option :"))
        if op==1:
            ad_panel()
        elif op==2:
            main_menu()
        elif op==3:
            break 

admin()