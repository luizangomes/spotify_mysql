from classesCP import Podcast, Episodio, Genero, Gravadora, Artista, Album, Usuario, Musica, Playlist
from conexao import MySQL



class UsuarioDAO():
    def __init__(self):
        pass
    
    def create(self, Usuario):
        try:
            dados = {'cpfUsuario': Usuario.cpfUsuario,
                     'nomeUsuario': Usuario.nomeUsuario,
                     'senhaUsuario': Usuario.senhaUsuario,
                     'emailUsuario': Usuario.emailUsuario,
                     'dataNascUsuario': Usuario.dataNascUsuario,
                     'tipoUsuario': Usuario.tipoUsuario,
                     'imgUsuario': Usuario.imgUsuario}
            sql = ("INSERT INTO USUARIO (cpfUsuario, nomeUsuario, senhaUsuario, emailUsuario, dataNascUsuario, tipoUsuario, imgUsuario) VALUES (%(cpfUsuario)s, %(nomeUsuario)s, %(senhaUsuario)s, %(emailUsuario)s, %(dataNascUsuario)s, %(tipoUsuario)s, %(imgUsuario)s)")
            self.conn(sql, dados)
            return dict(message='Usuario created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM USUARIO"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def delete(self, cpfUsuario):
        try:
            sql = "DELETE FROM USUARIO WHERE cpfUsuario = %s" % (cpfUsuario)
            self.conn(sql, dados=None)
            return dict(message='Usuario deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Usuario, cpfUsuario):
        try:
            sql = "UPDATE USUARIO SET nomeUsuario = %(nomeUsuario)s, senhaUsuario = %(senhaUsuario)s, emailUsuario = %(emailUsuario)s, dataNascUsuario = %(dataNascUsuario)s, tipoUsuario = %(tipoUsuario)s, imgUsuario = %(imgUsuario)s WHERE cpfUsuario = %(cpfUsuario)s"
            dados = {'nomeUsuario': Usuario.nomeUsuario,
                     'senhaUsuario': Usuario.senhaUsuario,
                     'emailUsuario': Usuario.emailUsuario,
                     'dataNascUsuario': Usuario.dataNascUsuario,
                     'tipoUsuario': Usuario.tipoUsuario,
                     'imgUsuario': Usuario.imgUsuario,
                     'cpfUsuario': cpfUsuario}
            self.conn(sql, dados)
            return dict(message='Usuario updated')
        except Exception as e:
            return dict(message=e.message)

    def search(self, cpfUsuario):
        try:
            sql = "SELECT nomeUsuario, senhaUsuario, dataNascUsuario, tipoUsuario, imgUsuario FROM USUARIO WHERE cpfUsuario = %s" % (cpfUsuario)
            result = self.conn_r(sql)
            nomeUsuario, senhaUsuario, dataNascUsuario, tipoUsuario, imgUsuario = result[0]
            usu = Usuario()
            usu.nomeUsuario = nomeUsuario
            usu.senhaUsuario = senhaUsuario
            usu.dataNascUsuario = dataNascUsuario
            usu.tipoUsuario = tipoUsuario
            usu.imgUsuario = imgUsuario
            return usu
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



class GravadoraDAO():
    def __init__(self):
        pass

    def create(self, Gravadora):
        try:
            dados = {'nomeGravadora': Gravadora.nomeGravadora,
                     'bioGravadora': Gravadora.bioGravadora,
                     'dataGravadora': Gravadora.dataGravadora,
                     'statusGravadora': Gravadora.statusGravadora,
                     'paisGravadora': Gravadora.paisGravadora}
            sql = ("INSERT INTO GRAVADORA (nomeGravadora, bioGravadora, dataGravadora, statusGravadora, paisGravadora)"
                    "VALUES (%(nomeGravadora)s, %(bioGravadora)s, %(dataGravadora)s, %(statusGravadora)s, %(paisGravadora)s)")
            self.conn(sql, dados)
            return dict(message='Gravadora created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM GRAVADORA"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def delete(self, codGravadora):
        try:
            sql = "DELETE FROM GRAVADORA WHERE codGravadora = %d" % (codGravadora)
            self.conn(sql, dados=None)
            return dict(message='Gravadora deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Gravadora, codGravadora):
        try:
            sql = "UPDATE GRAVADORA SET nomeGravadora = %(nomeGravadora)s, bioGravadora = %(bioGravadora)s, dataGravadora = %(dataGravadora)s, statusGravadora = %(statusGravadora)s, paisGravadora = %(paisGravadora)s WHERE codGravadora = %(codGravadora)s"
            dados = {'nomeGravadora': Gravadora.nomeGravadora,
                     'bioGravadora': Gravadora.bioGravadora,
                     'dataGravadora': Gravadora.dataGravadora,
                     'statusGravadora': Gravadora.statusGravadora,
                     'paisGravadora': Gravadora.paisGravadora,
                     'codGravadora': codGravadora}
            self.conn(sql, dados)
            return dict(message='Gravadora updated')
        except Exception as e:
            return dict(message=e.message)

    def search(self, codGravadora):
        try:
            sql = "SELECT nomeGravadora, bioGravadora, dataGravadora, statusGravadora, paisGravadora FROM GRAVADORA WHERE codGravadora = %s" % (codGravadora)
            result = self.conn_r(sql)
            nomeGravadora, bioGravadora, dataGravadora, statusGravadora, paisGravadora = result[0]
            gra = Gravadora()
            gra.nomeGravadora = nomeGravadora
            gra.bioGravadora = bioGravadora
            gra.dataGravadora = dataGravadora
            gra.statusGravadora = statusGravadora
            gra.paisGravadora = paisGravadora
            return gra
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



class ArtistaDAO():
    def __init__(self):
        pass

    def create(self, Artista):
        try:
            dados = {'nomeArtista': Artista.nomeArtista,'tipoArtista': Artista.tipoArtista, 'statusArtista': Artista.statusArtista, 'paisArtista': Artista.paisArtista, 'imgArtista': Artista.imgArtista, 'codArtista': Artista.codArtista, 'codGravadora': Artista.codGravadora}
            sql = ("insert into ARTISTA (nomeArtista, tipoArtista, statusArtista, paisArtista, imgArtista, codGravadora) values (%(nomeArtista)s, %(tipoArtista)s, %(statusArtista)s, %(paisArtista)s, %(imgArtista)s, %(codGravadora)s)")
            self.conn(sql, dados)
            return dict(message='Artista created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM ARTISTA"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def delete(self, codArtista):
        try:
            sql = "DELETE FROM ARTISTA WHERE codArtista = %d" % (codArtista)
            self.conn(sql, dados=None)
            return dict(message='Artista deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Artista, codArtista):
        try:
            sql = "UPDATE ARTISTA SET nomeArtista = %(nomeArtista)s, tipoArtista = %(tipoArtista)s, statusArtista = %(statusArtista)s, paisArtista = %(paisArtista)s, paisArtista = %(paisArtista)s, imgArtista = %(imgArtista)s, codGravadora = %(codGravadora)s WHERE codArtista = %(codArtista)s"
            dados = {'nomeArtista': Artista.nomeArtista,
                     'tipoArtista': Artista.tipoArtista,
                     'statusArtista': Artista.statusArtista,
                     'paisArtista': Artista.paisArtista,
                     'imgArtista': Artista.imgArtista,
                     'codGravadora': Artista.codGravadora,
                     'codArtista': codArtista}
            self.conn(sql, dados)
            return dict(message='Artista updated')
        except Exception as e:
            return dict(message=e.message)

    def search(self, codArtista):
        try:
            sql = "SELECT nomeArtista, tipoArtista, statusArtista, paisArtista, imgArtista, codGravadora FROM ARTISTA WHERE codArtista = %s" % (codArtista)
            result = self.conn_r(sql)
            nomeArtista, tipoArtista, statusArtista, paisArtista, imgArtista, codGravadora = result[0]
            art = Artista()
            art.nomeArtista = nomeArtista
            art.tipoArtista = tipoArtista
            art.statusArtista = statusArtista
            art.paisArtista = paisArtista
            art.imgArtista = imgArtista
            art.codGravadora = codGravadora
            return art
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



class AlbumDAO():
    def __init__(self):
        pass

    def create(self, Album):
        try:
            dados = {'nomeAlbum': Album.nomeAlbum,'tipoAlbum': Album.tipoAlbum, 'dataAlbum': Album.dataAlbum, 'imgAlbum': Album.imgAlbum, 'codAlbum': Album.codAlbum, 'codArtista': Album.codArtista, 'codGravadora': Album.codGravadora}
            sql = ("insert into ALBUM (nomeAlbum, tipoAlbum, dataAlbum, imgAlbum, codArtista, codGravadora) values (%(nomeAlbum)s, %(tipoAlbum)s, %(dataAlbum)s, %(imgAlbum)s, %(codArtista)s, %(codGravadora)s)")
            self.conn(sql, dados)
            return dict(message='Album created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM ALBUM"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def delete(self, codAlbum):
        try:
            sql = "DELETE FROM ALBUM WHERE codAlbum = %d" % (codAlbum)
            self.conn(sql, dados=None)
            return dict(message='Album deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Album, codAlbum):
        try:
            sql = "UPDATE ALBUM SET nomeAlbum = %(nomeAlbum)s, tipoAlbum = %(tipoAlbum)s, dataAlbum = %(dataAlbum)s, imgAlbum = %(imgAlbum)s, codArtista = %(codArtista)s, codGravadora = %(codGravadora)s WHERE codAlbum = %(codAlbum)s"
            dados = {'nomeAlbum': Album.nomeAlbum,
                     'tipoAlbum': Album.tipoAlbum,
                     'dataAlbum': Album.dataAlbum,
                     'imgAlbum': Album.imgAlbum,
                     'codArtista': Album.codArtista,
                     'codGravadora': Album.codGravadora,
                     'codAlbum': codAlbum}
            self.conn(sql, dados)
            return dict(message='Album updated')
        except Exception as e:
            return dict(message=e.message)

    def search(self, codAlbum):
        try:
            sql = "SELECT nomeAlbum, tipoAlbum, dataAlbum, imgAlbum, codArtista, codGravadora FROM ALBUM WHERE codAlbum = %s" % (codAlbum)
            result = self.conn_r(sql)
            nomeAlbum, tipoAlbum, dataAlbum, imgAlbum, codArtista, codGravadora = result[0]
            alb = Album()
            alb.nomeAlbum = nomeAlbum
            alb.tipoAlbum = tipoAlbum
            alb.dataAlbum = dataAlbum
            alb.imgAlbum = imgAlbum
            alb.codArtista = codArtista
            alb.codGravadora = codGravadora
            return alb
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



class MusicaDAO():
    def __init__(self):
        pass

    def create(self, Musica):
        try:
            dados = {'nomeMusica': Musica.nomeMusica,
                     'compositor': Musica.compositor,
                     'produtor': Musica.produtor,
                     'durMusica': Musica.durMusica,
                     'codAlbum': Musica.codAlbum,
                     'codGenero': Musica.codGenero}
            sql = ("INSERT INTO MUSICA (nomeMusica, compositor, produtor, durMusica, codAlbum, codGenero)"
                    "VALUES (%(nomeMusica)s, %(compositor)s, %(produtor)s, %(durMusica)s, %(codAlbum)s, %(codGenero)s)")
            self.conn(sql, dados)
            return dict(message='Musica created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM MUSICA"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def delete(self, codMusica):
        try:
            sql = "DELETE FROM MUSICA WHERE codMusica = %d" % (codMusica)
            self.conn(sql, dados=None)
            return dict(message='Musica deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Musica, codMusica):
        try:
            sql = "UPDATE MUSICA SET nomeMusica = %(nomeMusica)s, compositor = %(compositor)s, produtor = %(produtor)s, durMusica = %(durMusica)s, codAlbum = %(codAlbum)s, codGenero = %(codGenero)s WHERE codMusica = %(codMusica)s"
            dados = {'nomeMusica': Musica.nomeMusica,
                     'compositor': Musica.compositor,
                     'produtor': Musica.produtor,
                     'durMusica': Musica.durMusica,
                     'codAlbum': Musica.codAlbum,
                     'codGenero': Musica.codGenero,
                     'codMusica': codMusica}
            self.conn(sql, dados)
            return dict(message='Musica updated')
        except Exception as e:
            return dict(message=e.message)

    def search(self, codMusica):
        try:
            sql = "SELECT nomeMusica, compositor, produtor, durMusica, codAlbum, codGenero FROM MUSICA WHERE codMusica = %s" % (codMusica)
            result = self.conn_r(sql)
            nomeMusica, compositor, produtor, durMusica, codAlbum, codGenero = result[0]
            mus = Musica()
            mus.nomeMusica = nomeMusica
            mus.compositor = compositor
            mus.produtor = produtor
            mus.durMusica = durMusica
            mus.codAlbum = codAlbum
            mus.codGenero = codGenero
            return mus
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




class PlaylistDAO():
    def __init__(self):
        pass

    def create(self, Playlist):
        try:
            dados = {'nomePlaylist': Playlist.nomePlaylist,
                     'descPlaylist': Playlist.descPlaylist,
                     'statusPlaylist': Playlist.statusPlaylist,
                     'imgPlaylist': Playlist.imgPlaylist,
                     'cpfUsuario': Playlist.cpfUsuario}
            sql = ("INSERT INTO PLAYLIST (nomePlaylist, descPlaylist, statusPlaylist, imgPlaylist, cpfUsuario) VALUES (%(nomePlaylist)s, %(descPlaylist)s, %(statusPlaylist)s, %(imgPlaylist)s, %(cpfUsuario)s)")
            self.conn(sql, dados)
            return dict(message='Playlist created')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        try:
            sql = "SELECT * FROM PLAYLIST"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def delete(self, codPlaylist):
        try:
            sql = "DELETE FROM PLAYLIST WHERE codPlaylist = %d" % (codPlaylist)
            self.conn(sql, dados=None)
            return dict(message='Playlist deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Playlist, codPlaylist):
        try:
            sql = "UPDATE PLAYLIST SET nomePlaylist = %(nomePlaylist)s, descPlaylist = %(descPlaylist)s, statusPlaylist = %(statusPlaylist)s, imgPlaylist = %(imgPlaylist)s, cpfUsuario = %(cpfUsuario)s WHERE codPlaylist = %(codPlaylist)s"
            dados = {'nomePlaylist': Playlist.nomePlaylist,
                     'descPlaylist': Playlist.descPlaylist,
                     'statusPlaylist': Playlist.statusPlaylist,
                     'imgPlaylist': Playlist.imgPlaylist,
                     'cpfUsuario': Playlist.cpfUsuario,
                     'codPlaylist': codPlaylist}
            self.conn(sql, dados)
            return dict(message='Playlist updated')
        except Exception as e:
            return dict(message=e.message)

    def search(self, codPlaylist):
        try:
            sql = "SELECT nomePlaylist, descPlaylist, statusPlaylist, imgPlaylist, cpfUsuario FROM PLAYLIST WHERE codPlaylist = %s" % (codPlaylist)
            result = self.conn_r(sql)
            nomePlaylist, descPlaylist, statusPlaylist, imgPlaylist, cpfUsuario = result[0]
            pla = Playlist()
            pla.nomePlaylist = nomePlaylist
            pla.descPlaylist = descPlaylist
            pla.statusPlaylist = statusPlaylist
            pla.imgPlaylist = imgPlaylist
            pla.cpfUsuario = cpfUsuario
            return pla
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



class PodcastDAO():
    def __init__(self):
        pass

    def create(self, Podcast):
        try:
            dados = {'nomePodcast': Podcast.nomePodcast, 
                     'generoPodcast': Podcast.generoPodcast, 
                     'classificacaoPodcast': Podcast.classificacaoPodcast, 
                     'paisPodcast': Podcast.paisPodcast, 
                     'imgPodcast': Podcast.imgPodcast}
            sql = ("INSERT INTO PODCAST (nomePodcast, generoPodcast, classificacaoPodcast, paisPodcast, imgPodcast)" 
                    "VALUES (%(nomePodcast)s, %(generoPodcast)s, %(classificacaoPodcast)s, %(paisPodcast)s, %(imgPodcast)s)")
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

    def delete(self, codPodcast):
        try:
            sql = "DELETE FROM PODCAST WHERE codPodcast = %d" % (codPodcast)
            self.conn(sql, dados=None)
            return dict(message='Podcast deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Podcast, codPodcast):
        try:
            sql = "UPDATE  PODCAST SET nomePodcast = %(nomePodcast)s, generoPodcast = %(generoPodcast)s, classificacaoPodcast = %(classificacaoPodcast)s, paisPodcast = %(paisPodcast)s, imgPodcast = %(imgPodcast)s WHERE codPodcast = %(codPodcast)s"
            dados = {'nomePodcast': Podcast.nomePodcast, 
                     'generoPodcast': Podcast.generoPodcast, 
                     'classificacaoPodcast': Podcast.classificacaoPodcast, 
                     'paisPodcast': Podcast.paisPodcast, 
                     'imgPodcast': Podcast.imgPodcast,
                     'codPodcast': codPodcast,}
            self.conn(sql, dados)
            return dict(message='Podcast updated')
        except Exception as e:
            return dict(message=e.message)
    
    def search(self, codPodcast):
        try:
            sql = "SELECT nomePodcast, generoPodcast, classificacaoPodcast, paisPodcast, imgPodcast FROM PODCAST WHERE codPodcast = %s" % (codPodcast)
            result = self.conn_r(sql)
            nomePodcast, generoPodcast, classificacaoPodcast, paisPodcast, imgPodcast = result[0]
            pod = Podcast()
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



class EpisodioDAO():
    def __init__(self):
        pass

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

    def delete(self, codEpisodio):
        try:
            sql = "DELETE FROM EPISODIO WHERE codEpisodio = %d" % (codEpisodio)
            self.conn(sql, dados=None)
            return dict(message='Episodio deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Episodio, codEpisodio):
        try:
            sql = "UPDATE  EPISODIO SET nomeEpisodio = %(nomeEpisodio)s, dataLancEpisodio = %(dataLancEpisodio)s, descEpisodio = %(descEpisodio)s, durEpisodio = %(durEpisodio)s, codPodcast = %(codPodcast)s WHERE codEpisodio = %(codEpisodio)s"
            dados = {'nomeEpisodio': Episodio.nomeEpisodio,
                     'dataLancEpisodio': Episodio.dataLancEpisodio, 
                     'descEpisodio': Episodio.descEpisodio, 
                     'durEpisodio': Episodio.durEpisodio, 
                     'codPodcast': Episodio.codPodcast,
                     'codEpisodio': codEpisodio}
            self.conn(sql, dados)
            return dict(message='Episodio updated')
        except Exception as e:
            return dict(message=e.message)

    def search(self, codEpisodio):
        try:
            sql = "SELECT nomeEpisodio, dataLancEpisodio,descEpisodio, durEpisodio, codPodcast FROM EPISODIO WHERE codEpisodio = %s" % (codEpisodio)
            result = self.conn_r(sql)
            nomeEpisodio, dataLancEpisodio,descEpisodio, durEpisodio, codPodcast = result[0]
            epi = Episodio()
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



class GeneroDAO():
    def __init__(self):
        pass

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

    def delete(self, codGenero):
        try:
            sql = "DELETE FROM GENERO WHERE codGenero = %d" % (codGenero)
            self.conn(sql, dados=None)
            return dict(message='Genero deleted')
        except Exception as e:
            return dict(message=e.message)

    def update(self, Genero, codGenero):
        try:
            sql = "UPDATE GENERO SET nomeGenero = %(nomeGenero)s, descGenero = %(descGenero)s, subGenero = %(subGenero)s, imgGenero = %(imgGenero)s WHERE codGenero = %(codGenero)s"
            dados = {'nomeGenero': Genero.nomeGenero,
                     'descGenero': Genero.descGenero, 
                     'subGenero': Genero.subGenero,
                     'imgGenero': Genero.imgGenero,
                     'codGenero': codGenero}
            self.conn(sql, dados)
            return dict(message='Genero updated')
        except Exception as e:
            return dict(message=e.message)
    
    def search(self, codGenero):
        try:
            sql = "SELECT nomeGenero, descGenero, subGenero, imgGenero FROM GENERO WHERE codGenero = %s" % (codGenero)
            result = self.conn_r(sql)
            nomeGenero, descGenero, subGenero, imgGenero = result[0]
            gen = Genero()
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