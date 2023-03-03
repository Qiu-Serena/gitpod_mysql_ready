import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Animali")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute ("CREATE TABLE Mammiferi (Id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(255), Razza VARCHAR(255), Peso (int), Eta (int)))

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Id, Nome_Proprio (varchar), Razza (varchar), Peso (int), Eta (int)) VALUES (%s, %s,%s,%s)"
val = ("", "Highway 21")
("John", "Highway 21")
("John", "Highway 21")
("John", "Highway 21")
("John", "Highway 21")
("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")