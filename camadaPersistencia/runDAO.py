from classesCP import Podcast, Episodio, Genero
from conexao import MySQL
from DAO import PodcastDAO, EpisodioDAO, GeneroDAO

class RunPodcast:
    def __init__(self):
        self.podcastDAO = PodcastDAO()

    def inputCreatePodcast(self):
        addPodcast = Podcast()
        print("Insira os dados do novo Podcast:")
        addPodcast.nomePodcast = input("Nome do Episódio:   ")
        addPodcast.generoPodcast = input("Gênero do Podcast:    ")
        addPodcast.classificacaoPodcast = input("Classificação de Podcast:  ")
        addPodcast.paisPodcast = input("País de Origem: ")
        addPodcast.imgPodcast = input("Importar imagem:"    )
        newPodcast = PodcastDAO()
        result = newPodcast.create(addPodcast)
        print(result)
    
    def readPodcast(self, codPodcast):
        podcasts = self.podcastDAO.read()
        results = []
        if codPodcast == 0:
            for iterate in podcasts:
                a, b, c, d, e, f = iterate
                podcasts = {'codPodcast': a, 'nomePodcast': b, 'generoPodcast': c, 'classificacaoPodcast': d, 'paisPodcast': e, 'imgPodcast': f}
                results.append(podcasts)
            for r in results:
                print(r)
        else:
            for iterate in podcasts:
                a, b, c, d, e, f = iterate
                podcasts = {'codPodcast': a, 'nomePodcast': b, 'generoPodcast': c, 'classificacaoPodcast': d, 'paisPodcast': e, 'imgPodcast': f}
                if a == codPodcast:
                    results.append(podcasts)
            for r in results:
                print(r)

    
    def inputUpdatePodcast(self, codPodcast):
        updatePodcast = Podcast
        print("Dados para serem atualizados:")
        updatePodcast.nomePodcast = input("Nome do Podcast: ")
        updatePodcast.generoPodcast = input("Gênero do Podcast: ")
        updatePodcast.classificacaoPodcast = input("Classificação de Podcast:   ")
        updatePodcast.paisPodcast = input("País de Origem: ")
        updatePodcast.imgPodcast = input("Importar imagem:  ")
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
        results = []
        if codEpisodio == 0:
            for iterate in episodes:
                a, b, c, d, e, f = iterate
                episodes = {'codEpisodio': a, 'nomeEpisodio': b, 'dataLancEpisodio': c, 'descEpisodio': d, 'durEpisodio': e, 'codPodcast': f}
                results.append(episodes)
            for r in results:
                print(r)
        else:
            for iterate in episodes:
                a, b, c, d, e, f = iterate
                episodes = {'codEpisodio': a, 'nomeEpisodio': b, 'dataLancEpisodio': c, 'descEpisodio': d, 'durEpisodio': e, 'codPodcast': f}
                if a == codEpisodio:
                    results.append(episodes)
            for r in results:
                print(r)

    
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
        addGenero.imgGenero = input("Imagem: ")
        newGenero = GeneroDAO()
        result = newGenero.create(addGenero)
        print(result)
    
    def readGenero(self, codGenero):
        genres = self.generoDAO.read()
        results = []
        if codGenero == 0:
            for iterate in genres:
                a, b, c, d, e = iterate
                genres = {'codGenero': a,'imgGenero': b, 'descGenero': c, 'subGenero': d, 'nomeGenero': e}
                results.append(genres)
            for r in results:
                print(r)
        else:
            for iterate in genres:
                a, b, c, d, e = iterate
                genres = {'codGenero': a,'imgGenero': b, 'descGenero': c, 'subGenero': d, 'nomeGenero': e}
                if a == codGenero:
                    results.append(genres)
            for r in results:
                print(r)

    
    def inputUpdateGenero(self, codGenero):
        updateGenero = Genero
        print("Dados para serem atualizados:")
        updateGenero.nomeGenero = input("Nome do Genero:   ")
        updateGenero.subGenero = input("Sub-Generos:    ")
        updateGenero.descGenero = input("Descrição:  ")
        updateGenero.imgGenero = input("Imagem: ")
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
