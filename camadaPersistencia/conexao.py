import mysql.connector
import MySQLdb

class MySQL():

    def __init__(self):
        pass

    def get_conexao(self):
        _host = 'localhost'
        _user="root"
        _passwd="Ghost91870817#"
        _name="SPOTIFY_FINAL"
        db = MySQLdb.connect(_host, _user, _passwd, _name)
        return db