import pyautogui
from time import sleep

#ALGUMAS INFORMAÇÕES IMPORTANTES PARA O FUNCIONAMENTO DO PROGAMA:
#
#1. As coordernadas de onde o mouse deverá clicar variam de tela para tela e de acordo de onde o a tela de login estará posicionada e devem ser configuradas com ajuda do mouseInfo
#
#2. Não altere o nome do arquivo txt ou estará sujeito a erros no programa
#
#3. Este é um programa simples porém funcional de automoção de tarefas, como por exemplo o cadastro de usuários
#
#4. Espero que gostem :)

#Abre o arquivo onde estão as informações dos usuários
with open('Usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        #Seleciona o nome do usuário de acordo com a linha do arquivo
        usuario = linha.split(':')[1]
        pyautogui.click(1149,43, duration=1) #Clica no campo selecionado de acordo com as coordenadas estabelecidas
        pyautogui.write(usuario) #Digita o nome do usuário
        pyautogui.click(1124,67, duration=1)
        next(arquivo) #Pula para próxima linha do arquivo
        senha = linha.split(':')[1]
        pyautogui.write(senha) #Digita a senha do usuário
        pyautogui.click(1199,98, duration=1) #Clica no botão para cadastrar
        next(arquivo)
