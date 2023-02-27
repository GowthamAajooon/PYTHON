import mysql.connector
from prettytable import from_db_cursor

conn = mysql.connector.connect(user='root', password='12345678', host='localhost',port='3308', database='customer')
cursor = conn.cursor()





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
                        print("Enter pid: ", end="")
                        a1 = int(input())
                        if a1>0 and a1<16: 
                            print("Enter quan: ", end="")
                            a2 = int(input())
                            sql = "INSERT INTO buy (CID,PID,QUAN,IS_PAID,PURCHASE_DATE) VALUES (%s, %s, %s,%s,date_format(now(),'%d-%m-%y'))"
                            val = (customer, a1, a2,"NOT PAID")

                            cursor.execute(sql, val)
                            break
                        else:
                            print("AVAILABLE FROM 1 TO 15")
                        
                    elif a == 2:
                        customer = int(input("Enter CID :"))
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
                        
                            else:
                                print("AVAILABLE FROM 1 TO 15")
                        break
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
                s = f"SELECT p.PNAME AS 'PRODUCT_NAME',p.PRICE AS PRICE,b.QUAN,p.PRICE * b.QUAN as 'AMOUNT' FROM buy as b inner join products as p using(PID) where CID={a} and IS_PAID='NOT PAID'"
                cursor.execute(s)
                print(from_db_cursor(cursor))
                print("\nTotal bill :",s2)
                pay = int(input("Pay the bill amuont: "))
                if str(pay)==str(s2):
                        print("Bill is paid Successfully")
                        ss2 = f"UPDATE buy SET IS_PAID = 'PAID' WHERE CID = {a}"
                        cursor.execute(ss2)
                        k=1
                else:
                        print("Enter the correct amount")
                        k=0
            else:
                print("No bill for you")
                break
        
    
    if inp == 4:
        break

conn.commit()
conn.close()   


