import game 
import sys
import time
import os
import io
import json
import random
from pynput.keyboard import Key, Listener
import pynput.keyboard as keyb
import threading
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'

try:
    import winsound
except ImportError or ModuleNotFoundError:
    print("Failed to import Winsound. Using FakeWinsound Instead")
    winsound = game.FakeWinsound()

def play_tone(frequency, duration):
    winsound.Beep(frequency, duration)
    time.sleep(duration / 1000)

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

BASE_DIR = (os.path.join(os.path.dirname(__file__)))
with open(rf'{BASE_DIR}\assets\game_foods.json', 'r') as file:
    default_items = json.load(file)

with open(rf'{BASE_DIR}\assets\more_items.json', 'r') as file:
    custom_items = json.load(file)

with open(rf'{BASE_DIR}\assets\save.json', 'r') as file:
    save_file = json.load(file)

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
        winsound.Beep(1000, 500)
        selecionadotrabalho = input("""
                    Qual seu trabalho? 
                [1] - Trabalho Inicial- Salário = 500
                [2] - Desempregado
                [3] - Faculdade       
                Insira a Opção: """)
        if selecionadotrabalho == "1":
            trabalho = "Trabalho Inicial"
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
            chance = random.randint(0,3)
            if chance > 1:
                self.loja.add_item(item["name"], item["value"], item["quantidade"], item["classe"], item["saturacao"])
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
        if key == keyb.KeyCode.from_char('s'):
            self.save_warning()
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
        [3] - IR AO MÉDICO
        [4] - TRABALHAR
                         
        INSIRA A OPÇÃO: """)
        stringio.write(data)
        sys.stdout.write(data)
        sys.stdout.flush()
        
        resposta = input("")

        if resposta == "1":
            self.loja.list_items(self.jogador)
            print(f"SEU DINHEIRO: {self.jogador.dinheiro}")
            item_tobuy = input("Que item deseja comprar (Use o nome do item)? ")
            quantity_tobuy = int(input("Qual quantidade deseja comprar? "))
            self.jogador.comprar_item(self.loja, item_tobuy, quantity_tobuy)
        elif resposta == "2":
            self.jogador.comer()
        elif resposta == "3":
            self.jogador.ir_ao_medico()
        elif resposta == "4":
            self.jogador.trabalhar()
        

    def _grow_up_task(self):
        self.jogador.crescer()
        for _, item in default_items.items():
            chance = random.randint(0,3)
            if chance > 1:
                self.loja.add_item(item["name"], item["value"], 0, item["classe"], item["saturacao"])
        
        self.loja.random_restock(4, 6)
        if len(custom_items['custom_items']) > 0:
            for _, item in custom_items['custom_items'].items():
                chance = random.randint(1, 5)
                if chance >= 0:
                    self.loja.add_item((item['name']), item['value'], random.randint(1,5), item['classe'], item['saturacao'])
        time.sleep(10)
        self.debounce = False
    
    def ajudashow(self):
        os.system("cls")
        string = (f'''
            [?] -- AJUDA -- [?]
        * CASO NÃO SAIBA JOGAR O JOGO, ESSE MENU ENSINA OS COMANDOS BÁSICOS:

        * [Alt Gr] - ABRE O MENU DE AJUDA

        * [Right Shift / Shift Direito] - ABRE O MENU DE STATUS ATUAIS.                         

        * [F12] - Abre o menu de ações
        
        * [Shift] - Cresce +1 de idade.
                  
        * [S] - Aperte S para salvar.


''')
        print(string)
        beep_ringtone_keep()

        
    def save_game(self):
        try:
            playerdata = save_file["PlayerData"]
            playerstorages = save_file["PlayerStorages"]

            data = {}
            data["ShopData"] = {}
            num = 0
            for shop in self.loja.inst:
                num += 1
                data["ShopData"][str(num)] = shop.items
            
  
            playerdata = {}
            playerdata["status"] = {}

            playerdata["nome"] = self.jogador.nome
            playerdata["idade"] = self.jogador.idade
            playerdata["trabalho"] = self.jogador.trabalho
            playerdata["salario"] = self.jogador.salario
            playerdata["dinheiro"] = self.jogador.dinheiro
            playerdata["status"]["saude"] = self.jogador.saude
            playerdata["status"]["fome"] = self.jogador.fome
            playerdata["status"]["energia"] = self.jogador.energia

            playerstorages = {}
            playerstorages["PlayerStorages"] = {}

            playerstorages["PlayerStorages"]["geladeira"] = self.jogador.geladeira
            playerstorages["PlayerStorages"]["armazenamento"] = self.jogador.armazenamento

            jsonloader = {
                "active":True,
                "PlayerData": playerdata,

                "PlayerStorages": playerstorages,

                "ShopData": data,
                }
            jsonfile = json.dumps(jsonloader, indent=4)
            with open(rf'{BASE_DIR}\assets\save.json', 'w') as f:
                f.write(jsonfile)
                print("Sucess...")
            sys.exit(1)
        except Exception as e:
            print(f"Failed to save: {e}")

    def save_warning(self):
        if save_file['active'] == False:
            print("[i] -- SEU ARQUIVO DE SAVE ESTÁ DESATIVADO. SOBREESCREVENDO SAVE ANTIGO. --[i]")
            print("(Ignore essa mensagem se essa for a primeira vez que você estiver jogando.")
            self.save_game()
        else:
            print("[I] ==== IMPORTANTE ==== [I]")
            inp = input("Um arquivo de save já foi encontrado. Deseja sobre-escrever ele? y/N")
            if inp.lower() == "y" or inp == "":
                self.save_game()
            else:
                print("Aboratando...")