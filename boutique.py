import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mysq001"
)

email = input("Email: ")
password = input("Password: ")

def insert_employee(Employee_Name,	Employee_Number,Employee_Email,	Employee_password):
    cursor = mydb.cursor()
    sql = "INSERT INTO employee(Employee_Name,	Employee_Number,	Employee_Email,	Employee_password) VALUES (%s,%s,%s)"
    val = (Employee_Name,	Employee_Number,Employee_Email,	Employee_password)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount,"employees Generated")
    
    
def del_employee():
    cursor = mydb.cursor()
    Email = input("Enter Email_Id: ")
    sql = "DELETE FROM employee WHERE Email = %s"
    val = (Email,)
    cursor.execute(sql,val)
    mydb.commit()
    print(cursor.rowcount,"employee delete ")

def view_employee():
    cursor = mydb.cursor()
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    employee = cursor.fetchall()
    if (employee): 
        for employee in employee:
            print(f"Id,Employee_Name,Employee_Number,Employee_Email,	Employee_password")
    else:
        print("No employees found.") 
    
def update_employee(Employee_Name,Employee_Number,Employee_Email,	Employee_password):
    cursor = mydb.cursor()
    sql = "UPDATE employee SET Employee_Name=%s,Employee_Number=%s,Employee_Email=%s,	Employee_password=%s WHERE Id =%s"
    val=(Employee_Name,Employee_Number,Employee_Email,	Employee_password) 
    cursor.execute(sql, val)
    mydb.commit()
    print("employees Details Updated Successfully.")
    

def customer_details(customer_Name	,customer_Phone,customer_Email	,customer_Password):
    cursor = mydb.cursor()
    sql = "INSERT INTO customer(customer_Name	,customer_Phone,customer_Email	,customer_Password) VALUES(%s, %s, %s, %s, %s)"
    val = (customer_Name	,customer_Phone,customer_Email	,customer_Password)
    cursor.execute(sql, val)
    mydb.commit()
    print("Registered Successfully.")

def view_customer(customer_Email	,customer_Password):
    cursor = mydb.cursor()
    sql = "SELECT * FROM customer WHERE customer_Email=%s and customer_Password=%s"
    val = (customer_Email	,customer_Password)
    cursor.execute(sql, val)
    correct = cursor.fetchall()

    if correct :
        print("Login Successfully.")
    else:
        print("Invalid Username.")

#def login():
 #   User_name = input("Enter your user name :-" )
 #   Password = input("Enter the password :-")
 #   view_customer(User_name, Password)  
 
 
def product_insert( product ,	product_Price	,product_Quantity ):
    cursor = mydb.cursor()
    sql = "INSERT INTO product(  product ,	product_Price	,product_Quantity  ) VALUES( %s, %s, %s)"
    val = ( product ,	product_Price	,product_Quantity )
    cursor.execute(sql, val)
    mydb.commit()
    print("Product Details Inserted Successfully.")
    
    
def display_product():
    cursor = mydb.cursor()
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    #product = cursor.fetchall()
    r=cursor.fetchall()
    for x in r:
        print(x)
        
def update_product(product ,	product_Price	,product_Quantity):
    cursor = mydb.cursor()
    sql = "UPDATE product SET product =%s,product_Price	=%s, product_Quantity=%s WHERE Id=%s"
    val=(product ,	product_Price	,product_Quantity) 
    cursor.execute(sql, val)
    mydb.commit()
    print("Product Details Updated Successfully.")
    
def update_details(Id):
    cursor = mydb.cursor()
    sql = "Update details SET Order_status = Done WHERE Id=%s"
    val = (Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Status Updated Successfully.")    


def view_details():
    cursor = mydb.cursor()
    sql = "SELECT * FROM details"   
    cursor.execute(sql)
    products = cursor.fetchall()
    if(products):
        for product in products:
            print(f"product_id	,Price	,Customer_id	,Quantity	,Order_status")
    else:
       print("no data")  
       
       
       
def admin_login(email, password):
    cursor = mydb.cursor()
    sql = "SELECT Email, password FROM employee WHERE Email = %s AND password = %s"
    cursor.execute(sql, ("admin@","admin"))
    result = cursor.fetchone()
    
    if result:
        return True
    else:
        return False
    
def employee_login(email, password):
    cursor = mydb.cursor()
    query = "SELECT Email, password FROM emplr WHERE Email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    
    if result:
        return True
    else:
        return False
   
   
if email=="admin@":
    admin_login(email, password)
    print("Welcome Admin")
    while True:
        print("\nFor inserting employee type 1 ")
        print("For deleting employee type 2 ")
        print("For update employee type 3 ")
        print("For view item type 4 ")
        print("for customer details type 5")
        print("For to exit 6 ")
        i=input()
        if i=="1":
            Employee_Name= input("Employee_Name:")
            Employee_Number=input("Employee_Number:")
            Employee_Email= input("Employee_Email:")
            Employee_password= input("Employee_password:")
            insert_employee()
        elif i=="2":
            Email= input("employee Email:")     
            del_employee()
        elif i=="3":
            Employee_Name= input("Employee_Name:")
            Employee_Number=input("Employee_Number:")
            Employee_Email= input("Employee_Email:")
            Employee_password= input("Employee_password:")
            update_employee()
        elif i=="4":
            product_id=input("product_id:")
            Price=input("Price:")
            Customer_id=input("Customer_id:")
            Quantity=input("Quantity:")
            Order_status=input("Order_status:")
            view_details()
        elif i =="5":
            customer_Name=input("customer_Name")
            customer_Phone=input("customer_Phone")
            customer_Email=input("customer_Email")
            customer_Password=input("customer_Password")
            customer_details()
        elif i =="6":
            print("Thankyou")
            break
        else:
            print("BYE")
            break

else:
    print("Invalid email or password")

