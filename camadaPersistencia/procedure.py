
from conexao import MySQL
from prettytable import PrettyTable

class Procedures():
    def __init__(self):
        pass
    def albumMusicas(self, cod):
        try:
            sql = "CALL sp_listaDeMusicasEmAlbum(%d)" % (cod)
            result = self.conn_r(sql)
            results = PrettyTable()
            results.field_names = ['codMusica', 'Título', 'Álbum', 'Artista', 'Duracao']
            for iterate in result:
                a, b, c, d, e  = iterate
                result = {a, b, c, d, e}
                row = ['%s'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e)]
                results.add_row(row)
            return results
        except Exception as e:
            return dict(message=e.message)

    def conn(self, sql, dados):
        conn = MySQL().get_conexao()
        cursor = conn.cursor()
        cursor.execute(sql, dados)
        conn.commit()
        cursor.close()
        conn.close()

    def conn_r(self, sql):
        conn = MySQL().get_conexao()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

#codAlbum =int(input("Escolha um Álbum para listar as músicas pertencentes: "))
#test = Procedures()
#result = test.biblioteca(codAlbum)
#print(result)