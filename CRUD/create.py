
import mysql.connector

connector = mysql.connector.connect(
  user="root",
  password="",
  database="SPOTIFY_FINAL"
)

cursor = connector.cursor()

sql = "insert into GRAVADORA(nomeGravadora, bioGravadora, dataGravadora, statusGravadora, paisGravadora) values (%s, %s, %s, %s, %s)"
data = ("Bertelsmann Music Group (BMG)", "Bertelsmann Music Group (abreviado como BMG) foi uma das seis divisões da empresa alemã Bertelsmann, formada em 1987 para englobar as atividades relacionadas às gravações musicais da empresa.", "2008-10-01", "ativa", "Estados Unidos da América")

cursor.execute(sql, data)
connector.commit()

cursor.close()
connector.close()

print(connector)