import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='123456'
)

#prepare a cursor onject
cursor = dataBase.cursor()

#create a database
cursor.execute("CREATE DATABASE  elderco")

print("Database created successfully")