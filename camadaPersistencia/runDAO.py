from classesCP import Podcast, Episodio, Genero, Gravadora
from conexao import MySQL
from DAO import PodcastDAO, EpisodioDAO, GeneroDAO, GravadoraDAO

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
        results = []
        if codGravadora == 0:
            for iterate in gravadoras:
                a, b, c, d, e, f = iterate
                gravadoras = {'codGravadora': a, 'nomeGravadora': b, 'bioGravadora': c, 'dataGravadora': d, 'statusGravadora': e, 'paisGravadora': f}
                results.append(gravadoras)   
            for r in results:
                print(r)
        else:
            for iterate in gravadoras:
                a, b, c, d, e, f = iterate
                gravadoras = {'codGravadora': a, 'nomeGravadora': b, 'bioGravadora': c, 'dataGravadora': d, 'statusGravadora': e, 'paisGravadora': f}
                if a == codGravadora:
                    results.append(gravadoras)
            for r in results:
                print(r)

    def inputDeleteGravadora(self, codGravadora):
        result = self.gravadoraDAO.delete(codGravadora)
        print(result)

Teste = RunGravadora()
const = int(input("Insira o código da Gravadora: "))
#Teste.inputCreateGravadora()
#Teste.readGravadora(const)
Teste.inputDeleteGravadora(const)


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
        addPodcast.imgPodcast = input("Importar imagem: ")
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
        podcast = self.podcastDAO.search(codPodcast)
        print("Dados para serem atualizados:")
        podcast.nomePodcast = input("Nome do Podcast: ")
        podcast.generoPodcast = input("Genero do Podcast: ")
        podcast.classificacaoPodcast = input("Classificação do Podcast: ")
        podcast.paisPodcast = input("País de Origem: ")
        podcast.imgPodcast = input("Importar imagem: ")
        updatePodcast = PodcastDAO()
        result = updatePodcast.update(podcast, codPodcast)
        print(result)
    
    def inputDeletePodcast(self, codPodcast):
        result = self.podcastDAO.delete(codPodcast)
        print(result)
    
#Teste = RunPodcast()
#codPodcastUpdate = int(input("Insira o código do Podcast: "))
#Teste.inputUpdatePodcast(codPodcast)
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
#const = int(input("Insira o código do Episodio:"))
#Teste.inputCreateGenero()
#Teste.inputDeleteGenero(const)
#Teste.readGenero(const)
#Teste.inputUpdateGenero(const)