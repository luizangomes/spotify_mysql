import PySimpleGUI as sg

sg.theme('Dark Amber')

layout = [[sg.Text("Interface básica do Micro Micro Spotify")], 
          [sg.Text("\n |\/|  o   _  ._   _     |\/|  o   _  ._   _    \n |   |  |  (_  |   (_)    |  |  |  (_  |   (_)   \n\n  __                      _     \n (_   ._    _   _|_  o _|_      \n __) |_)  (_)   |_  |   |   \/   \n       |                         /    \n")],
          [sg.Text("\n\nOlá, este é o Micro Micro Spotify, aqui podemos consultar, inserir, deletar e atualizar dados do nosso banco de dados.\nNo momento você gostaria de utilizar qual classe do banco de Dados? Escolha entre as disponíveis abaixo:\n(1)   Álbum\n(2)   Artista\n(3)   Concerto\n(4)   Episódio\n(5)   Gênero\n(6)   Gravadora\n(7)   Música\n(8)   Playlist\n(9)   Podcast\n(10)   Usuário\n(0) SAIR DO PROGRAMA\n(digite somente o número da classe escolhida)")],
          [sg.Text("INPUT = "), sg.InputText(size =(3, 1)), sg.Submit()]]


window = sg.Window("Micro Micro Spotify", layout)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()