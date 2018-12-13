import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",user="root",passwd="admin",database="employee_schema")

mycursor = conn.cursor()

mycursor.execute("select * from employee")

# print("Display all employees")
# for i in mycursor:
#     print(i)

# print("Display all employees using result variable")
# result = mycursor.fetchall()
# for i in result:
#     print(i)

print("Display first employee")
result = mycursor.fetchone()
for i in result:
    print(i)

conn.close()