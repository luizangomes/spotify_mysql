from classesCP import Podcast, Episodio, Genero
from conexao import MySQL

class PodcastDAO(Podcast):
    def __init__(self):
        self.codPodcast = ''
        self.nomePodcast = ''
        self.generoPodcast = ''
        self.classificacaoPodcast = ''
        self.paisPodcast = ''
        self.imgPodcast = ''

    def create(self, Podcast):
        try:
            dados = {'nomePodcast': Podcast.nomePodcast, 'generoPodcast': Podcast.generoPodcast, 'classificacaoPodcast': Podcast.classificacaoPodcast, 'paisPodcast': Podcast.paisPodcast, 'imgPodcast': Podcast.imgPodcast}
            sql = ("insert into PODCAST (nomePodcast, generoPodcast, classificacaoPodcast, paisPodcast, imgPodcast) values (%(nomePodcast)s, %(generoPodcast)s, %(classificacaoPodcast)s, %(paisPodcast)s, %(imgPodcast)s)")
            self.conn(sql, dados)
            return dict(message='Podcast created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM PODCAST"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def update(self, Podcast, codPodcast):
        try:
            sql = "UPDATE  PODCAST SET nomePodcast = %(nomePodcast)s, generoPodcast=%(generoPodcast)s, classificacaoPodcast=%(classificacaoPodcast)s, paisPodcast=%(paisPodcast)s, imgPodcast=%(imgPodcast)s) WHERE codPodcast= %(codPodcast)d"
            dados = {'codPodcast': codPodcast, 'nomePodcast': Podcast.nomePodcast, 'generoPodcast': Podcast.generoPodcast, 'classificacaoPodcast': Podcast.classificacaoPodcast, 'paisPodcast': Podcast.paisPodcast, 'imgPodcast': Podcast.imgPodcast}
            self.conn(sql, dados)
            return dict(message='Podcast updated')
        except Exception as e:
            return dict(message=e.message)

    def delete(self, codPodcast):
        try:
            sql = "DELETE FROM PODCAST WHERE codPodcast = %d" % (codPodcast)
            self.conn(sql, dados=None)
            return dict(message='Podcast deleted')
        except Exception as e:
            return dict(message=e.message)

    
    def search(self, Podcast, codPodcast):
        try:
            sql = "SELECT nomePodcast, generoPodcast,classificacaoPodcast, paisPodcast, imgPodcast FROM PODCAST where codPodcast = %d" % (codPodcast)
            result = self.conn_r(sql)
            nomePodcast, generoPodcast, classificacaoPodcast, paisPodcast, imgPodcast = result[0]
            pod = Podcast
            pod.nomePodcast = nomePodcast
            pod.generoPodcast = generoPodcast
            pod.classificacaoPodcast = classificacaoPodcast
            pod.paisPodcast = paisPodcast
            pod.imgPodcast = imgPodcast
            return pod
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



class EpisodioDAO(Episodio):
    def __init__(self):
        self.codEpisodio = ''
        self.nomeEpisodio = ''
        self.dataLancEpisodio = ''
        self.descEpisodio = ''
        self.durEpisodio = ''
        self.codPodcast = ''

    def create(self, Episodio):
        try:
            dados = {'nomeEpisodio': Episodio.nomeEpisodio,'dataLancEpisodio': Episodio.dataLancEpisodio, 'descEpisodio': Episodio.descEpisodio, 'durEpisodio': Episodio.durEpisodio, 'codEpisodio': Episodio.codEpisodio, 'codPodcast': Episodio.codPodcast}
            sql = ("insert into EPISODIO (nomeEpisodio, dataLancEpisodio, descEpisodio, durEpisodio, codPodcast) values (%(nomeEpisodio)s, %(dataLancEpisodio)s, %(descEpisodio)s, %(durEpisodio)s, %(codPodcast)s)")
            self.conn(sql, dados)
            return dict(message='Episodio created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM EPISODIO"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def update(self, Episodio, codEpisodio):
        try:
            sql = "UPDATE  EPISODIO SET nomeEpisodio = %(nomeEpisodio)s, dataLancEpisodio=%(dataLancEpisodio)s, descEpisodio=%(descEpisodio)s, durEpisodio=%(durEpisodio)s, codPodcast=%(codPodcast)d) WHERE codEpisodio = %d" % (codEpisodio)
            dados = {'nomeEpisodio': Episodio.nomeEpisodio,'dataLancEpisodio': Episodio.dataLancEpisodio, 'descEpisodio': Episodio.descEpisodio, 'durEpisodio': Episodio.durEpisodio, 'codEpisodio': Episodio.codEpisodio, 'codPodcast': Episodio.codPodcast}
            self.conn(sql, dados)
            return dict(message='Episodio updated')
        except Exception as e:
            return dict(message=e.message)

    def delete(self, codEpisodio):
        try:
            sql = "DELETE FROM EPISODIO WHERE codEpisodio = %d" % (codEpisodio)
            self.conn(sql, dados=None)
            return dict(message='Episodio deleted')
        except Exception as e:
            return dict(message=e.message)

    
    def search(self, Episodio, codEpisodio):
        try:
            sql = "SELECT nomeEpisodio, dataLancEpisodio,descEpisodio, durEpisodio, codPodcast FROM PODCAST where codEpisodio = %d" % (codEpisodio)
            result = self.conn_r(sql)
            nomeEpisodio, dataLancEpisodio,descEpisodio, durEpisodio, codPodcast = result[0]
            epi = Episodio
            epi.nomeEpisodio = nomeEpisodio
            epi.dataLancEpisodio = dataLancEpisodio
            epi.descEpisodio = descEpisodio
            epi.durEpisodio = durEpisodio
            epi.codPodcast = codPodcast
            return epi
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



class GeneroDAO(Genero):
    def __init__(self):
        self.codGenero = ''
        self.nomeGenero = ''
        self.subGenero = ''
        self.descGenero = ''
        self.imgGenero = ''

    def create(self, Genero):
        try:
            dados = {'imgGenero': Genero.imgGenero, 'descGenero': Genero.descGenero, 'subGenero': Genero.subGenero, 'nomeGenero': Genero.nomeGenero}
            sql = ("insert into GENERO (nomeGenero, descGenero, subGenero, imgGenero) values (%(nomeGenero)s, %(descGenero)s, %(subGenero)s, %(imgGenero)s)")
            self.conn(sql, dados)
            return dict(message='Genero created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM GENERO"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def update(self, Genero, codGenero):
        try:
            sql = "UPDATE GENERO SET nomeGenero = %(nomeGenero)s, descGenero=%(descGenero)s, subGenero=%(subGenero)s, imgGenero=%(imgGenero)s) WHERE codGenero = %d" % (codGenero)
            dados = {'imgGenero': Genero.imgGenero, 'descGenero': Genero.descGenero, 'subGenero': Genero.subGenero, 'nomeGenero': Genero.nomeGenero}
            self.conn(sql, dados)
            return dict(message='Genero updated')
        except Exception as e:
            return dict(message=e.message)

    def delete(self, codGenero):
        try:
            sql = "DELETE FROM GENERO WHERE codGenero = %d" % (codGenero)
            self.conn(sql, dados=None)
            return dict(message='Genero deleted')
        except Exception as e:
            return dict(message=e.message)

    
    def search(self, Genero, codGenero):
        try:
            sql = "SELECT codGenero, nomeGenero, descGenero, subGenero, imgGenero FROM GENERO where codGenero = %d" % (codGenero)
            result = self.conn_r(sql)
            codGenero, nomeGenero, descGenero, subGenero, imgGenero = result[0]
            gen = Genero
            gen.nomeGenero = nomeGenero
            gen.descGenero = descGenero
            gen.subGenero = subGenero
            gen.imgGenero = imgGenero
            return gen
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