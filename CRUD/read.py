
import mysql.connector

connection = mysql.connector.connect(
  user="root",
  password="",
  database="SPOTIFY_FINAL"
)

cursor = connection.cursor()

sql = "SELECT * FROM GRAVADORA"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
  print(result)