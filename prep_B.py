import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza , Peso, Eta ) VALUES (%s, %s,%s,%s)"
val = [
("Alessio", "cane", 18, 18),
("John", "gatto", 20,10),
("Ben", "pappagallo",30,5),
("Carlo", "coniglio",20,20),
("Dom", "lucertola",10,10),
("Lei", "leone",50,19)
]

mycursor.executemany(sql, val)

mydb.commit()

