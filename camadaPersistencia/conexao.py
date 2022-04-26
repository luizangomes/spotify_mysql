import MySQLdb

class MySQL:
    def __init__(self):
        pass

    def get_conexao(self):
        _host = 'localhost'
        _user="root"
        _passwd=""
        _name="SPOTIFY_FINAL"
        db = MySQLdb.connect(_host, _user, _passwd, _name)
        return db