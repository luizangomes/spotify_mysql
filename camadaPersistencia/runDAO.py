from classesCP import Podcast, Episodio, Genero
from conexao import MySQL
from DAO import PodcastDAO

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
    
    def readPodcast(self):
        podcasts = self.podcastDAO.read()
        results = []
        for iterate in podcasts:
            a, b, c, d, e, f = iterate
            podcasts = {'codPodcast': a, 'nomePodcast': b, 'generoPodcast': c, 'classificacaoPodcast': d, 'paisPodcast': e, 'imgPodcast': f}
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

    
Teste = RunPodcast()
#codPodcastUpdate = int(input("Insira o código do Podcast à ser deletado:"))
#Teste.inputDeletePodcast(codPodcastUpdate)
#Teste.inputCreatePodcast()
#Teste.readPodcast()
    

