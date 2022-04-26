from classesCP import Podcast, Episodio, Genero
from DAO import PodcastDAO, EpisodioDAO, GeneroDAO
from prettytable import PrettyTable
from blobMaker import BlobSolver


class RunPodcast:
    def __init__(self):
        self.podcastDAO = PodcastDAO()

    def inputCreatePodcast(self):
        addPodcast = Podcast()
        print("Insira os dados do novo Podcast:")
        addPodcast.nomePodcast = input("Nome do Podcast:   ")
        addPodcast.generoPodcast = input("Gênero do Podcast:    ")
        addPodcast.classificacaoPodcast = input("Classificação de Podcast:  ")
        addPodcast.paisPodcast = input("País de Origem: ")
        print("Importar imagem:"    )
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
                podcasts = {a,  b, c, d, e, f}
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
        updatePodcast = Podcast
        print("Dados para serem atualizados:")
        updatePodcast.nomePodcast = input("Nome do Podcast: ")
        updatePodcast.generoPodcast = input("Gênero do Podcast: ")
        updatePodcast.classificacaoPodcast = input("Classificação de Podcast:   ")
        updatePodcast.paisPodcast = input("País de Origem: ")
        bs = BlobSolver
        imgpath = bs.insertBLOB()
        updatePodcast.imgPodcast = bs.convertToBinaryData(imgpath)
        update = PodcastDAO()
        result = update.search(updatePodcast, codPodcast)
        print(result)
    
    def inputDeletePodcast(self, codPodcast):
        result = self.podcastDAO.delete(codPodcast)
        print(result)

    
#Teste = RunPodcast()
#codPodcastUpdate = int(input("Insira o código do Podcast à ser deletado:"))
#Teste.inputDeletePodcast(codPodcastUpdate)
#Teste.inputCreatePodcast()
#Teste.readPodcast(codPodcastUpdate)
    
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
        updateEpisodio = Episodio
        print("Dados para serem atualizados:")
        updateEpisodio.nomeEpisodio = input("Nome do Episódio:   ")
        updateEpisodio.dataLancEpisodio = input("Data de Lançamento:    ")
        updateEpisodio.descEpisodio = input("Descrição:  ")
        updateEpisodio.durEpisodio = input("Duração (hh:mm:ss): ")
        updateEpisodio.codPodcast = input("Código do Podcast:"    )
        update = PodcastDAO()
        result = update.search(updateEpisodio, codEpisodio)
        print(result)
    
    def inputDeleteEpisodio(self, codEpisodio):
        result = self.episodioDAO.delete(codEpisodio)
        print(result)

    
#Teste = RunEpisodio()
#Teste.inputCreateEpisodio()
#const = int(input("Insira o código do Episodio à ser deletado:"))
#Teste.inputDeleteEpisodio(codPodcastUpdate)
#Teste.readEpisodio(const)



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
        updateGenero = Genero
        print("Dados para serem atualizados:")
        updateGenero.nomeGenero = input("Nome do Genero:   ")
        updateGenero.subGenero = input("Sub-Generos:    ")
        updateGenero.descGenero = input("Descrição:  ")
        print("Imagem: ")
        bs = BlobSolver
        imgpath = bs.insertBLOB()
        updateGenero.imgGenero = bs.convertToBinaryData(imgpath)
        update = GeneroDAO()
        result = update.search(updateGenero, codGenero)
        print(result)
    
    def inputDeleteGenero(self, codGenero):
        result = self.generoDAO.delete(codGenero)
        print(result)

    
#Teste = RunGenero()
#Teste.inputCreateGenero()
#const = int(input("Insira o código do Episodio à ser deletado:"))
#Teste.inputDeleteEpisodio(codPodcastUpdate)
#Teste.readGenero(const)
