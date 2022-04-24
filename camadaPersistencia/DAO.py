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

"""
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
            dados = {'nomeEpisodio': Episodio.nomeEpisodio,'dataLancEpisodio': Episodio.dataLancEpisodio, 'descEpisodio': Episodio.descEpisodio, 'durEpisodio': Episodio.durEpisodio}
            sql = ("insert into EPISODIO (nomeEpisodio, dataLancEpisodio, descEpisodio, durEpisodio, codPodcast) values (%(nomeEpisodio)s, %(dataLancEpisodio)s, %(descEpisodio)s, %(durEpisodio)s, %(codPodcast)s)")
            self.conn(sql, dados)
            return dict(message='Podcast created')
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
            sql = "UPDATE  EPISODIO SET nomeEpisodio = %(nomePodcast)s, genero=%(generoPodcast)s, classificacaoPodcast=%(classificacaoPodcast)s, paisPodcast=%(paisPodcast)s, imgPodcast=%(imgPodcast)s) WHERE codPodcast= %(codPodcast)d"
            dados = {'nomeEpisodio': Episodio.nomeEpisodio,'dataLancEpisodio': Episodio.dataLancEpisodio, 'descEpisodio': Episodio.descEpisodio, 'durEpisodio': Episodio.durEpisodio}
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
""""