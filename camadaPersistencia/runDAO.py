from classesCP import Podcast, Episodio, Genero, Gravadora, Artista, Album
from DAO import PodcastDAO, EpisodioDAO, GeneroDAO, GravadoraDAO, ArtistaDAO, AlbumDAO
from prettytable import PrettyTable
from blobMaker import BlobSolver

class RunGravadora:
    def __init__(self):
        self.gravadoraDAO = GravadoraDAO()

    def inputCreateGravadora(self):
        addGravadora = Gravadora()
        print("Insira os dados da nova Gravadora: ")
        addGravadora.nomeGravadora = input("Nome da Gravadora: ")
        addGravadora.bioGravadora = input("Biografia da Gravadora: ")
        addGravadora.dataGravadora = input("Data de criação da Gravadora: ")
        addGravadora.statusGravadora = input("A Gravadora está ativa? ")
        addGravadora.paisGravadora = input("País de Origem: ")
        newGravadora = GravadoraDAO()
        result = newGravadora.create(addGravadora)
        print(result)

    def readGravadora(self, codGravadora):
        gravadoras = self.gravadoraDAO.read()
        results = PrettyTable()
        results.field_names = ['codGravadora', 'nomeGravadora', 'bioGravadora', 'dataGravadora', 'statusGravadora', 'paisGravadora']
        if codGravadora == 0:
            for iterate in gravadoras:
                a, b, c, d, e, f = iterate
                gravadoras = {a, b, c, d, e, f}
                gravadora = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e), '%s'%(f)]
                results.add_row(gravadora)   
            print(results)
        else:
            for iterate in gravadoras:
                a, b, c, d, e, f = iterate
                if a == codGravadora:
                    gravadoras = {a, b, c, d, e, f}
                    gravadora = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e), '%s'%(f)]
                    results.add_row(gravadora)
            print(results)

    def inputDeleteGravadora(self, codGravadora):
        result = self.gravadoraDAO.delete(codGravadora)
        print(result)

    def inputUpdateGravadora(self, codGravadora):
        gravadora = self.gravadoraDAO.search(codGravadora)
        print("Dados para serem atualizados: ")
        gravadora.nomeGravadora = input("Nome da Gravadora: ")
        gravadora.bioGravadora = input("Biografia da Gravadora: ")
        gravadora.dataGravadora = input("Data de criação da Gravadora (YYYY-MM-DD): ")
        gravadora.statusGravadora = input("Status da Gravadora (ativa/não ativa): ")
        gravadora.paisGravadora = input("País de Origem: ")
        updateGravadora = GravadoraDAO()
        result = updateGravadora.update(gravadora, codGravadora)
        print(result)


#Teste = RunGravadora()
#const = int(input("Insira o código da Gravadora: "))
#Teste.inputCreateGravadora()
#Teste.readGravadora(const)
#Teste.inputUpdateGravadora(const)
#Teste.inputDeleteGravadora(const)



class RunArtista:
    def __init__(self):
        self.artistaDAO = ArtistaDAO()

    def inputCreateArtista(self):
        addArtista = Artista()
        print("Insira os dados do(a) novo(a) Artista: ")
        addArtista.nomeArtista = input("Nome do(a) Artista: ")
        addArtista.tipoArtista = input("Tipo de Artista: ")
        addArtista.statusArtista = input("Status do(a) Artista: ")
        addArtista.paisArtista = input("País de Origem: ")
        print("Importar imagem: ")
        bs = BlobSolver
        imgpath = bs.insertBLOB()
        addArtista.imgArtista = bs.convertToBinaryData(imgpath)
        addArtista.codGravadora = input("Código da Gravadora: ")
        newArtista = ArtistaDAO()
        result = newArtista.create(addArtista)
        print(result)

    def readArtista(self, codArtista):
        artistas = self.artistaDAO.read()
        results = PrettyTable()
        results.field_names = ['codArtista', 'nomeArtista', 'tipoArtista', 'statusArtista', 'paisArtista', 'imgArtista', 'codGravadora']
        if codArtista == 0:
            for iterate in artistas:
                a, b, c, d, e, f, g = iterate
                podcasts = {a, b, c, d, e, f, g}
                artista = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e), '%s'%(f), '%s'%(g)]
                results.add_row(artista)   
            print(results)
        else:
            for iterate in artistas:
                a, b, c, d, e, f, g = iterate
                if a == codArtista:
                    artista = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e), '%s'%(f), '%s'%(g)]
                    results.add_row(artista)
            print(results)

    def inputDeleteArtista(self, codArtista):
        result = self.artistaDAO.delete(codArtista)
        print(result)

    def inputUpdateArtista(self, codArtista):
        artista = self.artistaDAO.search(codArtista)
        print("Dados para serem atualizados: ")
        artista.nomeArtista = input("Nome do(a) Artista: ")
        artista.tipoArtista = input("Tipo de Artista: ")
        artista.statusArtista = input("Status do(a) Artista: ")
        artista.paisArtista = input("País de Origem: ")
        artista.imgArtista = input("Importar imagem: ")
        artista.codGravadora = input("Código da Gravadora: ")
        updateArtista = ArtistaDAO()
        result = updateArtista.update(artista, codArtista)
        print(result)

#Teste = RunArtista()
#const = int(input("Insira o código do(a) Artista: "))
#Teste.inputCreateArtista()
#Teste.readArtista(const)
#Teste.inputUpdateArtista(const)
# Teste.inputDeleteArtista(const)



class RunAlbum:
    def __init__(self):
        self.albumDAO = AlbumDAO()

    def inputCreateAlbum(self):
        addAlbum = Album()
        print("Insira os dados do novo Álbum: ")
        addAlbum.nomeAlbum = input("Nome do Álbum: ")
        addAlbum.tipoAlbum = input("Tipo do Álbum: ")
        addAlbum.dataAlbum = input("Data de lançamento do Álbum (YYYY-MM-DD): ")
        addAlbum.imgAlbum = input("Importar imagem: ")
        addAlbum.codArtista = input("Código do Artista: ")
        addAlbum.codGravadora = input("Código da Gravadora: ")
        newAlbum = AlbumDAO()
        result = newAlbum.create(addAlbum)
        print(result)

    def readAlbum(self, codAlbum):
        albuns = self.albumDAO.read()
        results = []
        if codAlbum == 0:
            for iterate in albuns:
                a, b, c, d, e, f, g = iterate
                albuns = {'codAlbum': a, 'nomeAlbum': b, 'tipoAlbum': c, 'dataAlbum': d, 'imgAlbum': e, 'codArtista': f, 'codGravadora': g}
                results.append(albuns)   
            for r in results:
                print(r)
        else:
            for iterate in albuns:
                a, b, c, d, e, f, g = iterate
                albuns = {'codAlbum': a, 'nomeAlbum': b, 'tipoAlbum': c, 'dataAlbum': d, 'imgAlbum': e, 'codArtista': f, 'codGravadora': g}
                if a == codAlbum:
                    results.append(albuns)
            for r in results:
                print(r)

    def inputDeleteAlbum(self, codAlbum):
        result = self.albumDAO.delete(codAlbum)
        print(result)

    def inputUpdateAlbum(self, codAlbum):
        album = self.albumDAO.search(codAlbum)
        print("Dados para serem atualizados: ")
        album.nomeAlbum = input("Nome do Álbum: ")
        album.tipoAlbum = input("Tipo de Álbum: ")
        album.dataAlbum = input("Data de lançamento do Álbum (YYYY-MM-DD): ")
        album.imgAlbum = input("Importar imagem: ")
        album.codArtista = input("Código do Artista: ")
        album.codGravadora = input("Código da Gravadora: ")
        updateAlbum = AlbumDAO()
        result = updateAlbum.update(album, codAlbum)
        print(result)

#Teste = RunAlbum()
#const = int(input("Insira o código do Álbum: "))
#Teste.inputCreateAlbum()
#Teste.readAlbum(const)
#Teste.inputUpdateAlbum(const)
#Teste.inputDeleteAlbum(const)



class RunPodcast:
    def __init__(self):
        self.podcastDAO = PodcastDAO()

    def inputCreatePodcast(self):
        addPodcast = Podcast()
        print("Insira os dados do novo Podcast: ")
        addPodcast.nomePodcast = input("Nome do Podcast: ")
        addPodcast.generoPodcast = input("Gênero do Podcast: ")
        addPodcast.classificacaoPodcast = input("Classificação de Podcast: ")
        addPodcast.paisPodcast = input("País de Origem: ")
        print("Importar imagem: ")
        bs = BlobSolver
        imgpath = bs.insertBLOB()
        addPodcast.imgPodcast = bs.convertToBinaryData(imgpath)
        newPodcast = PodcastDAO()
        result = newPodcast.create(addPodcast)
        print(result)
    
    def readPodcast(self, codPodcast):
        podcasts = self.podcastDAO.read()
        results = PrettyTable()
        results.field_names = ['codPodcast', 'nomePodcast', 'generoPodcast', 'classificacaoPodcast', 'paisPodcast', 'imgPodcast']
        if codPodcast == 0:
            for iterate in podcasts:
                a, b, c, d, e, f = iterate
                podcasts = {a, b, c, d, e, f}
                podcast = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e), '%s'%(f)]
                results.add_row(podcast)
            print(results)
        else:
            for iterate in podcasts:
                a, b, c, d, e, f = iterate
                if a == codPodcast:
                    podcasts = {a, b, c, d, e, f}
                    podcast = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e), '%s'%(f)]
                    results.add_row(podcast)
            print(results)
    
    def inputUpdatePodcast(self, codPodcast):
        podcast = self.podcastDAO.search(codPodcast)
        print("Dados para serem atualizados: ")
        podcast.nomePodcast = input("Nome do Podcast: ")
        podcast.generoPodcast = input("Genero do Podcast: ")
        podcast.classificacaoPodcast = input("Classificação do Podcast: ")
        podcast.paisPodcast = input("País de Origem: ")
        print("Importar imagem: ")
        bs = BlobSolver
        imgpath = bs.insertBLOB()
        podcast.imgPodcast = bs.convertToBinaryData(imgpath)
        updatePodcast = PodcastDAO()
        result = updatePodcast.update(podcast, codPodcast)
        print(result)
    
    def inputDeletePodcast(self, codPodcast):
        result = self.podcastDAO.delete(codPodcast)
        print(result)
    
#Teste = RunPodcast()
#const = int(input("Insira o código do Podcast: "))
#Teste.inputCreatePodcast()
#Teste.readPodcast(const)
#Teste.inputUpdatePodcast(const)
#Teste.inputDeletePodcast(const)


    
class RunEpisodio:
    def __init__(self):
        self.episodioDAO = EpisodioDAO()

    def inputCreateEpisodio(self):
        addEpisodio = Episodio()
        print("Insira os dados do novo Episódio:")
        addEpisodio.nomeEpisodio = input("Nome do Episódio:   ")
        addEpisodio.dataLancEpisodio = input("Data de Lançamento:    ")
        addEpisodio.descEpisodio = input("Descrição:  ")
        addEpisodio.durEpisodio = input("Duração (hh:mm:ss): ")
        addEpisodio.codPodcast = input("Código do Podcast:"    )
        newEpisodio = EpisodioDAO()
        result = newEpisodio.create(addEpisodio)
        print(result)
    
    def readEpisodio(self, codEpisodio):
        episodes = self.episodioDAO.read()
        results = PrettyTable()
        results.field_names = ['codEpisodio', 'nomeEpisodio', 'dataLancEpisodio', 'descEpisodio', 'durEpisodio', 'codPodcast']
        if codEpisodio == 0:
            for iterate in episodes:
                a, b, c, d, e, f = iterate
                episodes = {a, b, c, d, e, f}
                episode = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e), '%s'%(f)]
                results.add_row(episode)
            print(results)
        else:
            for iterate in episodes:
                a, b, c, d, e, f = iterate
                if a == codEpisodio:
                    episodes = {a, b, c, d, e, f}
                    episode = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e), '%s'%(f)]
                    results.add_row(episode)
            print(results)

    def inputUpdateEpisodio(self, codEpisodio):
        episodio = self.episodioDAO.search(codEpisodio)
        print("Dados para serem atualizados:")
        episodio.nomeEpisodio = input("Nome do Episódio: ")
        episodio.dataLancEpisodio = input("Data de Lançamento: ")
        episodio.descEpisodio = input("Descrição: ")
        episodio.durEpisodio = input("Duração (hh:mm:ss): ")
        episodio.codPodcast = input("Código do Podcast: ")
        updateEpisodio = EpisodioDAO()
        result = updateEpisodio.update(episodio, codEpisodio)
        print(result)

    def inputDeleteEpisodio(self, codEpisodio):
        result = self.episodioDAO.delete(codEpisodio)
        print(result)
    
#Teste = RunEpisodio()
#const = int(input("Insira o código do Episodio: "))
#Teste.inputCreateEpisodio()
#Teste.inputDeleteEpisodio(const)
#Teste.readEpisodio(const)
#Teste.inputUpdateEpisodio(const)



class RunGenero:
    def __init__(self):
        self.generoDAO = GeneroDAO()

    def inputCreateGenero(self):
        addGenero = Genero()
        print("Insira os dados do novo Genero:")
        addGenero.nomeGenero = input("Nome do Genero:   ")
        addGenero.subGenero = input("Sub-Generos:    ")
        addGenero.descGenero = input("Descrição:  ")
        print("Imagem: ")
        bs = BlobSolver
        imgpath = bs.insertBLOB()
        addGenero.imgGenero = bs.convertToBinaryData(imgpath)
        newGenero = GeneroDAO()
        result = newGenero.create(addGenero)
        print(result)
    
    def readGenero(self, codGenero):
        genres = self.generoDAO.read()
        results = PrettyTable()
        results.field_names = ['codGenero','imgGenero', 'descGenero', 'subGenero', 'nomeGenero']
        if codGenero == 0:
            for iterate in genres:
                a, b, c, d, e = iterate
                genres = [a, b, c, d, e]
                genre = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e)]
                results.add_row(genre)
            print(results)
        else:
            for iterate in genres:
                a, b, c, d, e = iterate
                if a == codGenero:
                    genres = [a, b, c, d, e]
                    genre = ['%d'%(a), '%s'%(b), '%s'%(c), '%s'%(d), '%s'%(e)]
                    results.add_row(genre)
            print(results)

    def inputUpdateGenero(self, codGenero):
        genero = self.generoDAO.search(codGenero)
        print("Dados para serem atualizados: ")
        genero.nomeGenero = input("Nome do Gênero: ")
        genero.subGenero = input("Sub-Gêneros: ")
        genero.descGenero = input("Descrição do Gênero: ")
        print("Importar imagem: ")
        bs = BlobSolver
        imgpath = bs.insertBLOB()
        genero.imgGenero = bs.convertToBinaryData(imgpath)
        updateGenero = GeneroDAO()
        result = updateGenero.update(genero, codGenero)
        print(result)
    
    def inputDeleteGenero(self, codGenero):
        result = self.generoDAO.delete(codGenero)
        print(result)
    
#Teste = RunGenero()
#const = int(input("Insira o código do Gênero: "))
#Teste.inputCreateGenero()
#Teste.readGenero(const)
#Teste.inputUpdateGenero(const)
#Teste.inputDeleteGenero(const)