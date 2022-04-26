class Usuario():
    #Atributos privados
    def __init__(self):
        self.cpfUsuario = None
        self.nomeUsuario = None
        self.senhaUsuario = None
        self.dataNascUsuario = None
        self.tipoUsuario = None
        self.imgUsuario = None

class Gravadora():
    #Atributos privados
    def __init__(self):
        self.codGravadora = None
        self.nomeGravadora = None
        self.bioGravadora = None
        self.dataGravadora = None
        self.statusGravadora = None
        self.paisGravadora = None

class Artista():
    #Atributos privados
    def __init__(self):
        self.codArtista = None
        self.nomeArtista = None
        self.tipoArtista = None
        self.statusArtista = None
        self.paisArtista = None
        self.imgArtista = None
        self.codGravadora = None

class Album():
    #Atributos privados
    def __init__(self):
        self.codAlbum = None
        self.nomeAlbum = None
        self.tipoAlbum = None
        self.dataAlbum = None
        self.imgAlbum = None
        self.codArtista = None
        self.codGravadora = None

class Musica():
    #Atributos privados
    def __init__(self):
        self.codMusica = None
        self.nomeMusica = None
        self.compositor = None
        self.produtor = None
        self.durMusica = None
        self.codAlbum = None
        self.codGenero = None

class Playlist():
    #Atributos privados
    def __init__(self):
        self.codPlaylist = None
        self.nomePlaylist = None
        self.descPlaylist = None
        self.statusPlaylist = None
        self.imgPlaylist = None
        self.cpfUsuario = None

class Concerto():
    #Atributos privados
    def __init__(self):
        self.dataHoraConcerto = None
        self.localConcerto = None
        self.lotacaoConcerto = None
        self.valorConcerto = None
        self.imgConcerto = None

class Podcast():
    def __init__(self):
        self.codPodcast = ''
        self.nomePodcast = ''
        self.generoPodcast = ''
        self.classificacaoPodcast = ''
        self.paisPodcast = ''
        self.imgPodcast = ''

class Episodio():
    def __init__(self):
        self.codEpisodio = ''
        self.nomeEpisodio = ''
        self.dataLancEpisodio = ''
        self.descEpisodio = ''
        self.durEpisodio = ''
        self.codPodcast = ''

class Genero():
    def __init__(self):
        self.codGenero = ''
        self.nomeGenero = ''
        self.subGenero = ''
        self.descGenero = ''
        self.imgGenero = ''