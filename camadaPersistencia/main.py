from operator import gt
import os
from runDAO import RunPodcast, RunEpisodio, RunGenero, RunArtista, RunAlbum, RunUsuario

header ="\n |\/|  o   _  ._   _     |\/|  o   _  ._   _    \n |  |  |  (_  |   (_)    |  |  |  (_  |   (_)   \n\n  __                      _     \n (_   ._    _   _|_  o  _|_      \n __)  |_)  (_)   |_  |   |   \/   \n      |                      /    \n"


def crudInterface():
    print("\n\nOlá, este é o Micro Micro Spotify, aqui podemos consultar, inserir, deletar e atualizar dados do nosso banco de dados.\nNo momento você gostaria de utilizar qual classe do banco de Dados? Escolha entre as disponíveis abaixo:\n(1)   Álbum\n(2)   Artista\n(3)   Concerto\n(4)   Episódio (OK)\n(5)   Gênero (OK)\n(6)   Gravadora\n(7)   Música\n(8)   Playlist\n(9)   Podcast (OK)\n(10)   Usuário\n(0) SAIR DO PROGRAMA\n(digite somente o número da classe escolhida)")
    value = input("ESCREVA O NÚMERO DA CLASSE ESCOLHIDA:  ")
    return value

print(header)

interromper = 0

while interromper == 0:
    classToCRUD = int(crudInterface())
    os.system('cls||clear')
    if classToCRUD == 1:
        print("ÁLBUM\n")
        albumCRUD = RunAlbum()
        alb = int(input("Escolha uma das funções que irá utilizar:\n(1) CRIAR\n(2) LER\n(3) ATUALIZAR\n(4) DELETAR\nINPUT = "))
        if alb == 1:
            albumCRUD.inputCreateAlbum()
        if alb == 2:
            escolha = int(input("Se gostaria de ver a lista geral de Gêneros insira 0, se for um gênero específico digite seu código\nINPUT = "))
            albumCRUD.readAlbum(escolha)
        if alb == 3:
            escolha = int(input("Escolha um gênero para atualizar, digite o seu código\nINPUT = "))
            albumCRUD.inputUpdateAlbum(escolha)
        if alb == 4:
            escolha = int(input("Escolha um gênero para deletar, digite o seu código\nINPUT = "))
            albumCRUD.inputDeleteAlbum(escolha)
    if classToCRUD == 4:
        print("EPISÓDIO\n")
        episodioCRUD = RunEpisodio()
        ep = int(input("Escolha uma das funções que irá utilizar:\n(1) CRIAR\n(2) LER\n(3) ATUALIZAR\n(4) DELETAR\nINPUT = "))
        if ep == 1:
            episodioCRUD.inputCreateEpisodio()
        if ep == 2:
            escolha = int(input("Se gostaria de ver a lista geral de Episódios insira 0, se for um episódio específico digite seu código\nINPUT = "))
            episodioCRUD.readEpisodio(escolha)
        if ep == 3:
            escolha = int(input("Escolha um episódio para atualizar, digite o seu código\nINPUT = "))
            episodioCRUD.inputUpdateEpisodio(escolha)
        if ep == 4:
            escolha = int(input("Escolha um episódio para deletar, digite o seu código\nINPUT = "))
            episodioCRUD.inputDeleteEpisodio(escolha)

    if classToCRUD == 5:
        print("GÊNERO\n")
        generoCRUD = RunGenero()
        gen = int(input("Escolha uma das funções que irá utilizar:\n(1) CRIAR\n(2) LER\n(3) ATUALIZAR\n(4) DELETAR\nINPUT = "))
        if gen == 1:
            generoCRUD.inputCreateGenero()
        if gen == 2:
            escolha = int(input("Se gostaria de ver a lista geral de Gêneros insira 0, se for um gênero específico digite seu código\nINPUT = "))
            generoCRUD.readGenero(escolha)
        if gen == 3:
            escolha = int(input("Escolha um gênero para atualizar, digite o seu código\nINPUT = "))
            generoCRUD.inputUpdateGenero(escolha)
        if gen == 4:
            escolha = int(input("Escolha um gênero para deletar, digite o seu código\nINPUT = "))
            generoCRUD.inputDeleteGenero(escolha)

    if classToCRUD == 9:
        print("PODCAST\n")
        podcastCRUD = RunPodcast()
        pod = int(input("Escolha uma das funções que irá utilizar:\n(1) CRIAR\n(2) LER\n(3) ATUALIZAR\n(4) DELETAR\nINPUT = "))
        if pod == 1:
            podcastCRUD.inputCreatePodcast()
        if pod == 2:
            escolha = int(input("Se gostaria de ver a lista geral de Podcasts insira 0, se for um podcast específico digite seu código\nINPUT = "))
            podcastCRUD.readPodcast(escolha)
        if pod == 3:
            escolha = int(input("Escolha um podcast para atualizar, digite o seu código\nINPUT = "))
            podcastCRUD.inputUpdatePodcast(escolha)
        if pod == 4:
            escolha = int(input("Escolha um podcast para deletar, digite o seu código\nINPUT = "))
            podcastCRUD.inputDeletePodcast(escolha)
    
    if classToCRUD == 10:
        print("USUÁRIO\n")
        usuarioCRUD = RunUsuario()
        us = int(input("Escolha uma das funções que irá utilizar:\n(1) CRIAR\n(2) LER\n(3) ATUALIZAR\n(4) DELETAR\nINPUT = "))
        if us == 1:
            usuarioCRUD.inputCreateUsuario()
        if us == 2:
            escolha = input("Se gostaria de ver a lista geral de usuários insira 0, se for um usuário específico insira 1: ")
            if escolha == '0':
                usuarioCRUD.readUsuario(int(escolha))
            elif escolha == '1':
                cpf = input("Insira o CPF do usuário: ")
                usuarioCRUD.readUsuario(cpf)
        if us == 3:
            escolha = int(input("Escolha um usuario para atualizar, digite o seu código\nINPUT = "))
            usuarioCRUD.inputUpdateUsuario(escolha)
        if us == 4:
            escolha = int(input("Escolha um usuario para deletar, digite o seu código\nINPUT = "))
            usuarioCRUD.inputDeleteUsuario(escolha)

    interromper = int(input("Você quer fechar o programa? (Digite: 1 - Sim ou 0 - Não)  "))
    os.system('cls||clear')
    if interromper == 1:
        break