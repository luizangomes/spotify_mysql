
import mysql.connector

connection = mysql.connector.connect(
  user="root",
  password="",
  database="SPOTIFY_FINAL"
)

cursor = connection.cursor()

read_gravadora = "SELECT * FROM GRAVADORA"

cursor.execute(read_gravadora)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
  print(result)