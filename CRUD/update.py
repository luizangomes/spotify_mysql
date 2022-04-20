
import mysql.connector
import datetime

connection = mysql.connector.connect(
  user="root",
  password="",
  database="SPOTIFY_FINAL"
)
cursor = connection.cursor()

update_gravadora = "UPDATE GRAVADORA SET nomeGravadora = %s, bioGravadora = %s,  dataGravadora = %s,  statusGravadora = %s,  paisGravadora = %s WHERE codGravadora = %s"
data = ("Bertelsmann Music Group (BMG)", "Bertelsmann Music Group (abreviado como BMG) foi uma das seis divisões da empresa alemã Bertelsmann, formada em 1987 para englobar as atividades relacionadas às gravações musicais da empresa", "2008-10-01", "ativa", "Estados Unidos da América", 2)

cursor.execute(update_gravadora, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros alterados")
