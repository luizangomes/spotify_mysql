
import mysql.connector

connection = mysql.connector.connect(
  user="root",
  password="",
  database="SPOTIFY_FINAL"
)

cursor = connection.cursor()

sql = "DELETE FROM GRAVADORA WHERE codGravadora = %s"
data = (1)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, "registros excluídos")
