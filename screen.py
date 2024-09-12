import game 
import winsound
import sys
import time
import os
import io
from pynput.keyboard import Key, Listener
import threading
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'

def play_tone(frequency, duration):
    winsound.Beep(frequency, duration)
    time.sleep(duration / 1000)
melody = [
    (392, 500), (440, 500), (494, 500), (523, 500), # G4, A4, B4, C5
    (494, 500), (440, 500), (392, 500),             # B4, A4, G4
    (440, 500), (494, 500), (523, 500), (587, 500), # A4, B4, C5, D5
    (523, 500), (494, 500), (440, 500),             # C5, B4, A4
]

def beep_error():
    winsound.Beep(100, 1500)
    time.sleep(1)
    os.system("cls")
def beep_warn():
    winsound.Beep(500, 500)
    time.sleep(1)
    os.system("cls")
def beep_ringtone():
    winsound.Beep(1000, 100)
    winsound.Beep(1500, 100)
    time.sleep(1)
    os.system("cls")
def beep_ringtone_keep():
    winsound.Beep(1000, 100)
    winsound.Beep(1500, 100)
def beep_ringtone_fast():
    winsound.Beep(1000, 100)
    winsound.Beep(1500, 100)
    os.system("cls")

def nuhuh():
    pass

default_items ={
    "Frango":{
        "name":"Frango",
        "quantidade":2,
        "value":550,
        "classe":"comida",
        "saturação":"boa"
    },
    "Batata":{
        "name":"Batata",
        "quantidade":5,
        "classe":"comida",
        "value":20,
        "saturação":"pouca"
    }
}




class StartGame:
    def __init__(self):
        pass
    def start(self):
        title =  ( RED +''' 
  _____ _   _ _____    ____    _    __  __ _____    ___  _____   _     ___ _____ _____ 
 |_   _| | | | ____|  / ___|  / \  |  \/  | ____|  / _ \|  ___| | |   |_ _|  ___| ____|
   | | | |_| |  _|   | |  _  / _ \ | |\/| |  _|   | | | | |_    | |    | || |_  |  _|  
   | | |  _  | |___  | |_| |/ ___ \| |  | | |___  | |_| |  _|   | |___ | ||  _| | |___ 
   |_| |_| |_|_____|  \____/_/   \_\_|  |_|_____|  \___/|_|     |_____|___|_|   |_____|''' + RESET +
   '''\n        BY YROD0200. VERSION 0.8                                       ''')
        print(f"{title} \n")
        winsound.Beep(1000, 100)
        winsound.Beep(1100, 100)
        nome = input("Qual seu nome? ")
        try:
            int(nome)
            print("Você é robô por acaso?")
            time.sleep(3)
            sys.exit(-1)
        except ValueError:
            nuhuh()
        if "Yuri".lower() in nome.lower():
            print("Não pode jogar comigo... Sei lá o que você vai me fazer fazer... Vou desligar por conta própia...")
            for note in melody:
                play_tone(note[0], note[1])
            sys.exit(-666)
        winsound.Beep(1000, 500)
        selecionadotrabalho = input("""
                    Qual seu trabalho? 
                [1] - Atendente do MC Donalds - Salário = 500
                [2] - Desempregado
                [3] - Faculdade       
                Insira a Opção: """)
        if selecionadotrabalho == "1":
            trabalho = "Atendente do MC Donalds"
            salario = 500
        elif selecionadotrabalho == "2":
            trabalho = "Desempregado"
            salario = 0
        elif selecionadotrabalho == "3":
            trabalho = "Faculdade"
            salario = 0
        else:
            print("Trabalho inválido... Será desempregado.")
            trabalho = "Desempregado"
            salario = 0
        try:
            player = game.Trabalhador(nome, 18, salario, trabalho, 1000)
            winsound.Beep(1000, 50)
            winsound.Beep(1100, 50)
        except:
            print("Falha ao iniciar o jogo. Fechando...")
            winsound.Beep(37, 1500)
            sys.exit(-1)
        print("\n\n O Jogo começou, aperte a tecla altgr para receber ajuda.")
        return player

class terminal_events():
    debounce = False
    def __init__(self, jogador):
        self.jogador = jogador  
        self.loja = game.Loja()
        for _, item in default_items.items():
            self.loja.add_item(item["name"], item["value"], item["quantidade"], item["classe"], item["saturação"])
        pass

        self.listen()
    def on_release(self, key):
        if key == Key.alt_gr:
            self.ajudashow()
        if key == Key.shift_r:
            self.status_print()
        if key == Key.shift_l:
            self.grow_up()
        if key == Key.f12:
            self.action_menu()
    def listen(self):
        with Listener(
            on_release=self.on_release
        ) as listener:
            listener.join()
    def status_print(self):
        self.jogador.showstatus()
    def grow_up(self):
        if not self.debounce:
            self.debounce = True
            threading.Thread(target=self._grow_up_task).start()
        else: 
            print("Você está fazendo coisas demais!")
    def action_menu(self):
        beep_ringtone_fast()
        stringio = io.StringIO()
        data = (""" 
        [.] -- MENU DE AÇÕES. FAÇA DE TUDO AQUI! -- [.]
        [1] - COMPRAR NA LOJA
        [2] - COMER ITEM (MAIS VELHO DA GELADEIRA.)
        [3] - IR AO MÉDICO (DISPONÍVEL UMA VEZ POR MINUTO.).
                         
        INSIRA A OPÇÃO: """)
        stringio.write(data)
        sys.stdout.write(data)
        sys.stdout.flush()
        
        resposta = input("")

        if resposta == "1":
            self.loja.list_items(self.jogador)
            item_tobuy = input("Que item deseja comprar (Use o nome do item)? ")
            quantity_tobuy = int(input("Qual quantidade deseja comprar? "))
            self.jogador.comprar_item(self.loja, item_tobuy, quantity_tobuy)
        elif resposta == "2":
            self.jogador.comer()
        elif resposta == "3":
            self.jogador.ir_ao_medico()
        

    def _grow_up_task(self):
        self.jogador.crescer()
        time.sleep(10)
        self.debounce = False
    
    def ajudashow(self):
        os.system("cls")
        string = (f'''
            [?] -- AJUDA -- [?]
        * CASO NÃO SAIBA JOGAR O JOGO, ESSE MENU ENSINA OS COMANDOS BÁSICOS:

        * [Alt Gr] - ABRE O MENU DE AJUDA

        * [Right Shift / Shift Direito] - ABRE O MENU DE STATUS ATUAIS.                         

        * [Alt] - Abre o menu de ações
        
        * [Shift] - Cresce +1 de idade.


''')
        print(string)
        beep_ringtone_keep()


