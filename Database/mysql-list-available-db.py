import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",user="root",passwd="admin")

mycursor = conn.cursor()

mycursor.execute("show databases")

print("Database connection has been created successfully. Display the list of database names available")
for i in mycursor:
    print(i)


conn.close()