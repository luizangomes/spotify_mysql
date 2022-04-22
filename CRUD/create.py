
import mysql.connector
def createGravadora():
  connector = mysql.connector.connect(
    user="root",
    password="",
    database="SPOTIFY_FINAL"
  )

  cursor = connector.cursor()

  create_gravadora = "insert into GRAVADORA(nomeGravadora, bioGravadora, dataGravadora, statusGravadora, paisGravadora) values (%s, %s, %s, %s, %s)"
  data = ("Gloob Gloob", "hkjjlgaUGQIUVQFL.", "2008-10-01", "ativa", "Brasil")

  cursor.execute(create_gravadora, data)
  connector.commit()

  cursor.close()
  connector.close()

  print(connector)