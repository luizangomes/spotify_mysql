import mysql.connector
header =" |\/|  o   _  ._   _     |\/|  o   _  ._   _    \n |  |  |  (_  |   (_)    |  |  |  (_  |   (_)   \n\n  __                      _     \n (_   ._    _   _|_  o  _|_      \n __)  |_)  (_)   |_  |   |   \/   \n      |                      /    \n"
def crudInterface():
    print("Olá, este é o Micro Micro Spotify, aqui podemos consultar, inserir, deletar e atualizar dados de nosso banco de dados\nNo momento você gostaria de utilizar qual classe do banco de Dados? Escolhe entre as disponíveis abaixo:\n(1)   Álbum\n(2)   Artista\n(3)   Concerto\n(4)   Episódio\n(5)   Gênero\n(6)   Gravadora\n(7)   Música\n(8)   Playlist\n(9)   Podcast\n(10)   Usuário\n(digite somente o número da classe escolhida)")
    value = input("ESCREVA O NÚMERO DA CLASSE ESCOLHIDA:  ")
    return value

print(header)
classToCRUD = crudInterface()

