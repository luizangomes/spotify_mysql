import PySimpleGUI as sg

class BlobSolver:
    def convertToBinaryData(filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    
    sg.theme('Dark Amber')
    layout = [[sg.Text("Cadastro de imagens:")], 
            [sg.Text("Procure o arquivo que gostaria de cadatrar:"), sg.FileBrowse(key="getImage"), sg.Submit()]]
    window = sg.Window("Micro Micro Spotify", layout)
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break
    window.close()
