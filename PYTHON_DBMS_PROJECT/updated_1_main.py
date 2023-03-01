import mysql.connector
from prettytable import from_db_cursor
conn = mysql.connector.connect(user='root', password='12345678', host='localhost',port='3308', database='customer')
cursor = conn.cursor()

t = 0
while True:
    print("""
          1. ADMIN
          2. USER
          3. Exit
          """)
    get_input = int(input("Enter to move : "))
    if get_input==1:
        admin_id = int(input("Enter ADMIN-ID :")) 
        admin_pwd = int(input("Enter ADMIN-PASSWORD :")) 
            # TO EXTRACT ADMINID AND ADMINPWD  
        sql = "SELECT * FROM admin"
        cursor.execute(sql)
        c1 = cursor.fetchall()
        for i in range(len(c1)):
            if c1[i][0]==admin_id and c1[i][1]==admin_pwd:
                while True:        
                    print("""
                        1. ADD PRODUCTS
                        2. UPDATE PRODUCTS
                        3. DELETE PRODUCTS 
                        4. EXIT
                        """)        
                    process = int(input("Enter to move :")) 
                    if process == 1: 
                            pid = int(input("Enter the PID :"))
                            sql1 = "SELECT * FROM products"
                            cursor.execute(sql1)
                            c1 = cursor.fetchall()
                            d1 = []
                            for i in range(len(c1)):
                                d1.append(c1[i][0])
                            if pid not in d1:
                                pname = input("Enter the PNAME :")
                                pquan = input("Enter the PQUAN :")
                                price = int(input("Enter the PRICE :"))
                                sql = "INSERT INTO products (PID,PNAME,PQUAN,PRICE) VALUES (%s,%s,%s,%s)"
                                val = (pid,pname,pquan,price)
                                cursor.execute(sql,val)
                                conn.commit()
                                print("\nADDED SUCCESSFULLY")
                            else:
                                print("Product id Already exists.\nUse different Product Id.")
                            
                                
                        
                            # print("Product id Already exists.\nUse different Product Id.")
                                
                    elif process == 2:
                        while True:                        
                            print("""
                                1. QUANTITY 
                                2. PRICE
                                3. EXIT
                                """) 
                            # pid = int(input("Enter the PID :"))
                            n = int(input("Enter to modify quan or price :"))
                            if n==1:
                                    pid = int(input("Enter the PID :"))
                                    sql = "SELECT * FROM products"
                                    cursor.execute(sql)
                                    c1 = cursor.fetchall()
                                    for i in range(len(c1)):
                                        if c1[i][0]==pid:        
                                            pquan = input("Enter the PQUAN :")
                                            sql = f"UPDATE products SET PQUAN='{pquan}' WHERE PID={pid}"
                                            cursor.execute(sql)
                                            conn.commit()
                                            print("QUANTITY ADDED SUCCESSFULLY")
                                            break                                    
                                    else:
                                        print("Enter Valid PID")
                                        
                            elif n==2:
                                pid = int(input("Enter the PID :"))
                                sql = "SELECT * FROM products"
                                cursor.execute(sql)
                                c1 = cursor.fetchall()
                                for i in range(len(c1)):
                                    if c1[i][0]==pid:        
                                        price = int(input("Enter the PRICE :"))
                                        sql = f"UPDATE products SET PRICE = {price} WHERE PID = {pid}"
                                        cursor.execute(sql)
                                        conn.commit()
                                        print("PRICE ADDED SUCCESSFULLY")
                                        break
                                else:
                                    print("Enter Valid PID")
                            elif n==3:
                                break
                                            
                    elif process == 3:
                        pid = int(input("Enter the PID :"))
                        sql = "SELECT * FROM products"
                        cursor.execute(sql)
                        c1 = cursor.fetchall()
                        for i in range(len(c1)):
                            if c1[i][0]==pid:                       
                                sql = f"DELETE FROM products WHERE PID = {pid}"
                                cursor.execute(sql)
                                conn.commit()
                                print("DELETED PRODUCT SUCCESSFULLY")
                                break
                        else:
                            print("Enter Valid PID")
                            
                    elif process == 4:
                        print("Thank You...")
                        break
                    
                                
        
    elif get_input==2:
        while True:
                
                print("""
                      1. SIGN UP
                      2. LOGIN 
                      3. Exit
                      """)
                get_input = int(input("Enter to move : "))
                if get_input==1:
                    try:
                        user_id = int(input())
                        password = int(input())
                            # print(user_id,password)
                        sql = "INSERT INTO signup (USER_CID,USER_PASSWORD,REGISTERED_DATE) VALUES (%s,%s,date_format(now(),'%d-%m-%y'))"
                        val = (user_id,password)
                        cursor.execute(sql, val)  
                        conn.commit()
                        print("Signuped succesfully")
                    except:
                        print("Customer Id already exists\nPlease Try different One")
                     
                elif get_input==2:
                    User_id = int(input("Enter User Id :"))
                    User_pwd = int(input("Enter User Password :"))
                    s1 = "select * from signup" 
                    cursor.execute(s1)
                    s2 = cursor.fetchall()
                    for i in range(len(s2)):
                        if s2[i][0]==User_id and s2[i][1]==User_pwd :
                            print("Access Granted....")
                            
                            while True:
                                print("""
                            1. AVAILABLE PRODUCTS
                            2. BUY PRODUCTS
                            3. DISPLAY BILL
                            4. EXIT
                            """)
                                inp = int(input())
            
                                if inp == 1:
                                    s = "SELECT * FROM products"
                                    cursor.execute(s)
                                    print(from_db_cursor(cursor))
            
                                elif inp == 2:
                                    while True:
                                        print("""
                            1. ADD
                            2. DELETE
                            3. EXIT
                                        """)
                                        f = int(input())
                                        if f == 1:
                                            while True:
                                                print('''
                            1.INSERT ONE
                            2.INSERT MANY
                            3.EXIT''')
                                                a = int(input())
                                                # customer = int(input("Enter CID :"))
                                                if a == 1:
                                                    customer = int(input("Enter CID :"))
                                                    
                                                    if customer==User_id:
                                                        print("Enter pid: ", end="")
                                                        a1 = int(input())
                                                        if a1>0 and a1<16: 
                                                            print("Enter quan: ", end="")
                                                            a2 = int(input())
                                                            sql = "INSERT INTO buy (CID,PID,QUAN,IS_PAID,PURCHASE_DATE) VALUES (%s, %s, %s,%s,date_format(now(),'%d-%m-%y'))"
                                                            val = (customer, a1, a2,"NOT PAID")
                
                                                            cursor.execute(sql, val)
                                                            conn.commit()
                                                            break
                                                        else:
                                                            print("AVAILABLE FROM 1 TO 15")
                                                    else:
                                                        print("Enter Correct Customer Id...")
                                                    
                                                elif a == 2:
                                                    customer = int(input("Enter CID :"))
                                                    if customer==User_id:
                                                        print("How many records ? :", end="")
                                                        r = int(input())
                                                        for i in range(r):
                                                            print("Enter pid: ", end="")
                                                            a1 = int(input())
                                                            if a1>0 and a1<16:
                                                                print("Enter quan: ", end="")
                                                                a2 = int(input())
                                                                sql = "INSERT INTO buy (CID,PID,QUAN,IS_PAID,PURCHASE_DATE) VALUES (%s, %s, %s,%s,date_format(now(),'%d-%m-%y'))"
                                                                val = (customer, a1, a2,"NOT PAID")   
                                                                cursor.execute(sql, val)
                                                                conn.commit()
                                                        
                                                            else:
                                                                print("AVAILABLE FROM 1 TO 15")
                                                        break
                                                    else:
                                                        print("Enter Correct Customer Id...")
                                                    
                                                else:
                                                    break
                                        elif f == 2:
                                            while True:
                                                print('''
                            1.DELETE ONE
                            2.DELETE MANY
                            3.EXIT''')
                                                a = int(input())
                                                if a == 1:
                                                    print("Enter buying pid: ", end="")
                                                    a1 = int(input())
                                                    if a1>0 and a1<16:
                                                        sql = f"DELETE FROM buy WHERE PID = {a1}"
                                                        cursor.execute(sql)
                                                        conn.commit()
                                                        break
                                                    else:
                                                        print("AVAILABLE FROM 1 TO 15")
                                                elif a == 2:
                                                    print("How many records ? :", end="")
                                                    r = int(input())
                                                    for i in range(r):
                                                        print("Enter buying pid :", end="")
                                                        a1 = int(input())
                                                        if a1>0 and a1<16:
                                                            sql = f"DELETE FROM buy WHERE PID = {a1}"
                                                            cursor.execute(sql)
                                                            conn.commit()
                                                        else:
                                                            print("AVAILABLE FROM 1 TO 15")
                                                    break
                                                else:
                                                    break
                                        elif f == 3:
                                            print("\nRETURN TO MAIN MENU\n")
                                            break
                                elif inp == 3:
                                    print("Bill details")
                                    a = int(input("Enter the CID: "))
                                    if a==User_id:
                                        s = f"SELECT p.PNAME AS 'PRODUCT_NAME',p.PRICE AS PRICE,b.QUAN,p.PRICE * b.QUAN as 'AMOUNT' FROM buy as b inner join products as p using(PID) where CID={a} and IS_PAID='NOT PAID'"
                                        cursor.execute(s)
                                        from_db_cursor(cursor)
                                        s1 = f"SELECT SUM(p.PRICE*b.QUAN) FROM products as p inner join buy as b using(PID) where b.CID = {a} AND b.IS_PAID = 'NOT PAID'" 
                                        cursor.execute(s1)
                                        s2 = str(list(cursor.fetchall()))
                                        s2 = s2.replace("'),)]",'')
                                        s2 = s2.replace("[(Decimal('",'')
                                        # print("\nTotal bill :",s2)
                                        k = 0
                                        while k==0:
                                            print()
                                            if s2.isnumeric():
                                                # s = f"SELECT p.PNAME AS 'PRODUCT_NAME',p.PRICE AS PRICE,b.QUAN,
                                                # p.PRICE * b.QUAN as 'AMOUNT' FROM buy as b inner join products as p 
                                                # using(PID) where CID={a} and IS_PAID='NOT PAID'"
                                                
                                                s = f"SELECT p.pname AS NAME, p.price AS PRICE, SUM(b.quan) as QUAN, SUM(b.quan * p.price) as AMOUNT FROM products as p inner JOIN buy as b using (pid) where b.cid={a} and b.is_paid = 'NOT PAID' GROUP BY p.pname, p.pquan, p.price;"
                                                
                                                cursor.execute(s)
                                                print(from_db_cursor(cursor))
                                                print("\nTotal bill :",s2)
                                                pay = int(input("Pay the bill amuont: "))
                                                if str(pay)==str(s2):
                                                        print("Bill is paid Successfully")
                                                        ss2 = f"UPDATE buy SET IS_PAID = 'PAID' WHERE CID = {a}"
                                                        cursor.execute(ss2)
                                                        conn.commit()
                                                        k=1
                                                else:
                                                        print("Enter the correct amount")
                                                        k=0
                                            else:
                                                print("No bill for you")
                                                break
                                    else:
                                        print("Enter Correct Customer Id...")
                                
                                if inp == 4:
                                    break
                            
                            
                        
                else:
                    break

        
    elif get_input==3:
        print("Thank You...")
        break
        
        
    
conn.commit()
conn.close()   
