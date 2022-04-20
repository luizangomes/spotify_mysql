
import mysql.connector

connection = mysql.connector.connect(
  user="root",
  password="",
  database="SPOTIFY_FINAL"
)

cursor = connection.cursor()

delete_gravadora = "DELETE FROM GRAVADORA WHERE codGravadora = %s"
data = (1)

cursor.execute(delete_gravadora, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, "registros excluídos")
