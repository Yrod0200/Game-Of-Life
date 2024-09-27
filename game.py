import copy
import math
import random
import json
import time
import os
import sys
import json
import math

class FakeWinsound:
    def __init__(self) -> None:
        pass
    def Beep(self, fake, fail):
        print("\b")

try:
    import winsound
except ImportError or ModuleNotFoundError:
    print("Failed to import Winsound. Using FakeWinsound Instead")
    winsound = FakeWinsound()

def beep_critical():
    winsound.Beep(57, 5000)
    time.sleep(2)
def beep_error():
    winsound.Beep(100, 1500)
    time.sleep(2)
    os.system("cls")
def beep_warn():
    winsound.Beep(500, 500)
    time.sleep(2)
    os.system("cls")
def beep_ringtone():
    winsound.Beep(1000, 100)
    winsound.Beep(1500, 100)
    time.sleep(3)
    os.system("cls")
def beep_ringtone_keep():
    winsound.Beep(1000, 100)
    winsound.Beep(1500, 100)
def beep_ringtone_fast():
    winsound.Beep(1000, 100)
    winsound.Beep(1500, 100)
    os.system("cls")
class Pessoa:
    instances = []
    def __init__(self, nome, idade):
        Pessoa.instances.append(self)
        self.nome = nome
        self.idade = idade
        self.saude = 100
        self.fome = 100
        self.energia = 100

    def demaior(self):
        if self.idade >= 18:
            return True
        else:
            return False

    def get_instances(self):
        print("[<>] -- PERSONAGENS -- [<>] \n")
        num = 0
        for instance in self.instances:
            num += 1
            print(f"{num}: Nome: {instance.nome}, Idade: {instance.idade} \n")

        
        
class Trabalhador(Pessoa):
    instances = []
    def __init__(self, nome, idade, salario, profissao, dinheiro):
        super().__init__(nome, idade)
        self.trabalho = profissao
        self.salario = salario 
        self.dinheiro = dinheiro
        self.armazenamento = {"maxslots":10, "espaco":{}}
        self.geladeira = {"maxslots":5, "espaco":{}}
        Trabalhador.instances.append(self)
        print(f"Seja bem vindo ao mundo, {self.nome}")

    def qualTrabalho(self):
        return self.trabalho
    
    def crescer(self):
        if self.idade > 110:
                           print(f"""              
                    ,----..      ,---,               ,'  , `.    ,---,.   
                    /   /   \    '  .' \           ,-+-,.' _ |  ,'  .' |   
                    |   :     :  /  ;    '.      ,-+-. ;   , ||,---.'   |   
                    .   |  ;. / :  :       \    ,--.'|'   |  ;||   |   .'   
                    .   ; /--`  :  |   /\   \  |   |  ,', |  '::   :  |-,   
                    ;   | ;  __ |  :  ' ;.   : |   | /  | |  ||:   |  ;/|   
                    |   : |.' .'|  |  ;/  \   \'   | :  | :  |,|   :   .'   
                    .   | '_.' :'  :  | \  \ ,';   . |  ; |--' |   |  |-,   
                    '   ; : \  ||  |  '  '--'  |   : |  | ,    '   :  ;/|   
                    '   | '/  .'|  :  :        |   : '  |/     |   |    \   
                    |   :    /  |  | ,'        ;   | |`-'      |   :   .'   
                    \   \ .'   `--''          |   ;/          |   | ,'     
                    `---`                    '---'           `----' ,---, 
                        ,----..                                    ,`--.' | 
                    /   /   \                  ,---,.,-.----.   |   :  : 
                    /   .     :        ,---.  ,'  .' |\    /  \  '   '  ; 
                    .   /   ;.  \      /__./|,---.'   |;   :    \ |   |  | 
                    .   ;   /  ` ; ,---.;  ; ||   |   .'|   | .\ : '   :  ; 
                    ;   |  ; \ ; |/___/ \  | |:   :  |-,.   : |: | |   |  ' 
                    |   :  | ; | '\   ;  \ ' |:   |  ;/||   |  \ : '   :  | 
                    .   |  ' ' ' : \   \  \: ||   :   .'|   : .  / ;   |  ; 
                    '   ;  \; /  |  ;   \  ' .|   |  |-,;   | |  \ `---'. | 
                    \   \  ',  /    \   \   ''   :  ;/||   | ;\  \ `--..`; 
                    ;   :    /      \   `  ;|   |    \:   ' | \.'.--,_    
                    \   \ .'        :   \ ||   :   .':   : :-'  |    |`. 
                        `---`           '---" |   | ,'  |   |.'    `-- -`, ;
                                            `----'    `---'        '---`" 

                      
                      
                - A hora da morte chega para todos um dia... {self.nome} morreu de Fome. -- [i]
                      """)
        else:
            self.idade += 1
            self.energia = 100
            random_hunger_decrease = random.randint(10, 30)
            self.fome -= random_hunger_decrease
            random_will_lose_health = random.randint(0, 3)
            if random_will_lose_health > 1:
                self.saude -= random.randint(1, 30)
            if self.fome <= 0:
                print(f"""            
                    ,----..      ,---,               ,'  , `.    ,---,.   
                    /   /   \    '  .' \           ,-+-,.' _ |  ,'  .' |   
                    |   :     :  /  ;    '.      ,-+-. ;   , ||,---.'   |   
                    .   |  ;. / :  :       \    ,--.'|'   |  ;||   |   .'   
                    .   ; /--`  :  |   /\   \  |   |  ,', |  '::   :  |-,   
                    ;   | ;  __ |  :  ' ;.   : |   | /  | |  ||:   |  ;/|   
                    |   : |.' .'|  |  ;/  \   \'   | :  | :  |,|   :   .'   
                    .   | '_.' :'  :  | \  \ ,';   . |  ; |--' |   |  |-,   
                    '   ; : \  ||  |  '  '--'  |   : |  | ,    '   :  ;/|   
                    '   | '/  .'|  :  :        |   : '  |/     |   |    \   
                    |   :    /  |  | ,'        ;   | |`-'      |   :   .'   
                    \   \ .'   `--''          |   ;/          |   | ,'     
                    `---`                    '---'           `----' ,---, 
                        ,----..                                    ,`--.' | 
                    /   /   \                  ,---,.,-.----.   |   :  : 
                    /   .     :        ,---.  ,'  .' |\    /  \  '   '  ; 
                    .   /   ;.  \      /__./|,---.'   |;   :    \ |   |  | 
                    .   ;   /  ` ; ,---.;  ; ||   |   .'|   | .\ : '   :  ; 
                    ;   |  ; \ ; |/___/ \  | |:   :  |-,.   : |: | |   |  ' 
                    |   :  | ; | '\   ;  \ ' |:   |  ;/||   |  \ : '   :  | 
                    .   |  ' ' ' : \   \  \: ||   :   .'|   : .  / ;   |  ; 
                    '   ;  \; /  |  ;   \  ' .|   |  |-,;   | |  \ `---'. | 
                    \   \  ',  /    \   \   ''   :  ;/||   | ;\  \ `--..`; 
                    ;   :    /      \   `  ;|   |    \:   ' | \.'.--,_    
                    \   \ .'        :   \ ||   :   .':   : :-'  |    |`. 
                        `---`           '---" |   | ,'  |   |.'    `-- -`, ;
                                            `----'    `---'        '---`" 

                      
                      
                - A hora da morte chega para todos um dia... {self.nome} morreu de Fome. -- [i]
                      """)
                beep_critical()
                os._exit(666)
            if self.saude < 0:
                print(f"""              
                    ,----..      ,---,               ,'  , `.    ,---,.   
                    /   /   \    '  .' \           ,-+-,.' _ |  ,'  .' |   
                    |   :     :  /  ;    '.      ,-+-. ;   , ||,---.'   |   
                    .   |  ;. / :  :       \    ,--.'|'   |  ;||   |   .'   
                    .   ; /--`  :  |   /\   \  |   |  ,', |  '::   :  |-,   
                    ;   | ;  __ |  :  ' ;.   : |   | /  | |  ||:   |  ;/|   
                    |   : |.' .'|  |  ;/  \   \'   | :  | :  |,|   :   .'   
                    .   | '_.' :'  :  | \  \ ,';   . |  ; |--' |   |  |-,   
                    '   ; : \  ||  |  '  '--'  |   : |  | ,    '   :  ;/|   
                    '   | '/  .'|  :  :        |   : '  |/     |   |    \   
                    |   :    /  |  | ,'        ;   | |`-'      |   :   .'   
                    \   \ .'   `--''          |   ;/          |   | ,'     
                    `---`                    '---'           `----' ,---, 
                        ,----..                                    ,`--.' | 
                    /   /   \                  ,---,.,-.----.   |   :  : 
                    /   .     :        ,---.  ,'  .' |\    /  \  '   '  ; 
                    .   /   ;.  \      /__./|,---.'   |;   :    \ |   |  | 
                    .   ;   /  ` ; ,---.;  ; ||   |   .'|   | .\ : '   :  ; 
                    ;   |  ; \ ; |/___/ \  | |:   :  |-,.   : |: | |   |  ' 
                    |   :  | ; | '\   ;  \ ' |:   |  ;/||   |  \ : '   :  | 
                    .   |  ' ' ' : \   \  \: ||   :   .'|   : .  / ;   |  ; 
                    '   ;  \; /  |  ;   \  ' .|   |  |-,;   | |  \ `---'. | 
                    \   \  ',  /    \   \   ''   :  ;/||   | ;\  \ `--..`; 
                    ;   :    /      \   `  ;|   |    \:   ' | \.'.--,_    
                    \   \ .'        :   \ ||   :   .':   : :-'  |    |`. 
                        `---`           '---" |   | ,'  |   |.'    `-- -`, ;
                                            `----'    `---'        '---`" 

                      
                      
                - A hora da morte chega para todos um dia... {self.nome} morreu de Sede. -- [i]
                      """)
                beep_critical()
                os._exit(666)
            print(f"{self.nome} cresceu com sucesso! Aperte Right Shift para ver seus novos atributos!")
            beep_ringtone()

    def ganhardinheiro(self, dinheiro):
        self.dinheiro += dinheiro

    def trabalhar(self):
        print(f"[i] -- {self.nome} foi trabalhar! --[i] ")
        beep_ringtone()
        if self.salario > 0:
            if self.energia > 10:
                print(f"[i] -- {self.nome} tem energia para trabalhar, trabalhando... -- [i]")
                beep_ringtone()
                self.energia -= 10
                self.dinheiro += self.salario / 24
                value = self.dinheiro
                self.dinheiro =  math.floor(value)
                print(f"[i] -- {self.nome} trabalhou com sucesso e recebeu seu salário de hora! seu dinheiro agora é: {self.dinheiro} --[i]")
                beep_ringtone_keep()
            else:
                print(f"[x]-- {self.nome} está cansado demais para trabalhar. --[x]")
        else:
            print(f"[x] -- {self.nome} não trabalha! -- [x]")
            beep_error()

    def get_food_value(self, value):
        if value == "podre":
            return -10
        if value == "pouca":
            return 10
        if value == "mediana":
            return 20
        if value == "boa":
            return 30
        if value == "perfeita" or value == "ceia":
            return 50
    def comer(self):
        self.mostrar_armazenavel("geladeira")
        if len(self.geladeira["espaco"]) > 0:
            comida = next(iter(self.geladeira["espaco"].items()))
            nome = comida[1]['name']
            print(f' \n [i] -- {self.nome} comeu {nome} --[i] \n ')
            beep_ringtone()
            if comida[1]['quantidade'] > 1:
                self.geladeira['espaco'][nome]['quantidade'] -= 1 
                food_value = self.geladeira['espaco'][nome]["saturacao"]
                new_food_value = self.get_food_value(food_value)
                self.fome += new_food_value
                if food_value == "podre":
                    print(f"\n [X] -- A comida {nome} estava podre. {self.nome} ficou com mais fome. --[X] \n ")
                    beep_error()
                else:
                    print(f'Agora está com: {self.fome} de alimento')
                    beep_ringtone()
                if self.fome > 100:
                    self.fome = 100
            else:
                food_value = self.geladeira['espaco'][nome]["saturacao"]
                new_food_value = self.get_food_value(food_value)
                new_food_value = self.get_food_value(food_value)
                self.fome += new_food_value
                if food_value == "podre":
                    print(f"\n [X] -- A comida {nome} estava podre. {self.nome} ficou com mais fome. --[X] \n ")
                    beep_error()
                else:
                    print(f'Agora está com: {self.fome} de alimento')
                    beep_ringtone()
                if self.fome > 100:
                    self.fome = 100
                del self.geladeira['espaco'][nome]
        else:
            print(f"Não tinha comida na geladeira. {self.nome} não recuperou nada")
            beep_warn()
    def pobre(self):
        if self.salario > 3000:
            return False
        else:
            return True
    def adicionar_item(self, item):
        if item["classe"] == "comida":
            if not len(self.geladeira["espaco"]) > self.geladeira["maxslots"]:
               if item["name"] not in self.geladeira["espaco"]:
                    self.geladeira["espaco"][item["name"]] = item
                    item_name  = item["name"]
                    print(f"\n [i] -- Adicionou {item_name} a geladeira. --[i] \n")
                    beep_ringtone()
               else:
                    self.geladeira["espaco"][item["name"]]["quantidade"] += item["quantidade"]
            else:
                print(f"{self.nome} tentou levar o item para casa, mas não tinha espaco disponível. Então ele teve que jogar fora.")
                beep_error()
        else:
            if not len(self.armazenamento["espaco"]) > self.armazenamento["maxslots"]:
               if item["name"] not in self.armazenamento["espaco"]:
                    self.armazenamento["espaco"][item["name"]] = item
                    item_name  = item["name"]
                    print(f"Adicionou {item_name} ao armazenamento.")
                    beep_warn()
               else:
                    self.geladeira["espaco"][item["name"]]["quantidade"] += item["quantidade"]
            else:
                print(f"{self.nome} tentou levar o item para casa, mas não tinha espaco disponível. Então ele teve que jogar fora.")
                beep_error()

    def mostrar_armazenavel(self, table):
        if table == "geladeira":
            value = self.geladeira["espaco"]
            print("\n [+] -- GELADEIRA -- [+] ")
        else:
            value = self.armazenamento["espaco"]
            print("\n [+] -- ARMAZENAMENTO -- [+] ")
        for _, item in value.items():
            name = item["name"]
            valor = item["quantidade"]
            print(f"{valor}x {name} \n")
            os
            beep_ringtone()
            os.system("cls")

    def comprar_item(self, lojaname, nome_do_item, quantidade):
        try:
            buying_shop = lojaname.items
            if buying_shop[nome_do_item]:
                print(f"\n [i] -- O ITEM {nome_do_item} EXISTE. -- [i]\n")
                beep_warn()
                if buying_shop[nome_do_item]["value"] * quantidade <= self.dinheiro:
                    if buying_shop[nome_do_item]["quantidade"] >= quantidade:   
                        self.dinheiro -= buying_shop[nome_do_item]["value"] * quantidade
                        buying_shop[nome_do_item]["quantidade"] -= quantidade
                        nome_do_item_comprado = buying_shop[nome_do_item]["name"]
                        print(f"\n [i] -- {self.nome} comprou {quantidade}x de {nome_do_item_comprado}. Levando para casa... --[i] \n")
                        beep_ringtone()
                        item_armazenavel = copy.deepcopy(buying_shop[nome_do_item])
                        dict.pop(item_armazenavel, "value")
                        item_armazenavel["quantidade"] = quantidade
                        try:
                            self.adicionar_item(item_armazenavel)
                        except Exception as e:
                            print(f"Error adding item: {e}")
                            beep_error()
                else:
                    print(f"\n [X] -- {self.nome} não conseguiu comprar item porque não tem dinheiro. Dinheiro na conta: {self.dinheiro}-- [X] ")
                    beep_error()
            else:
                print(f"\n [X] -- {self.nome} não conseguiu comprar item porque não havia no estoque. Aperte AltGr para o guia. -- [X]")
                beep_error()
        except:
            beep_critical()
            print("ERRO COMPRANDO ITEM.")
    def get_instances(self):
        print("[<>] -- TRABALHADORES -- [<>] \n")
        num = 1
        for instance in self.instances:
            print(f"{num}: Nome: {instance.nome}, Idade: {instance.idade}, Trabalho: {instance.trabalho} \n")
            num += 1
    def showstatus(self):
        os.system("cls")
        string = (f'''
            [!] -- STATUS DO JOGADOR -- [!]

                NOME: {self.nome}
                IDADE: {self.idade}
                TRABALHO: {self.trabalho}
                SALÁRIO: {self.salario}
                DINHEIRO NA CONTA BANCÁRIA: {self.dinheiro}

                --- STATUS DE VIDA ---
                FOME: {self.fome}
                SAUDE: {self.saude}
                ENERGIA: {self.energia}
            
            [!] ----------------------- [!]
''')
        print(string)
        beep_ringtone_keep()
    def ir_ao_medico(self):
        doencas = ["Doença n.1", "Doença n.2", "Deonça n.3"]
        doenca = random.choice(doencas)
        if self.saude < 75:
            print("[i] -- DOENÇA --[i]")
            print(f"{self.nome} foi diagnosticado com {doenca}")
            beep_ringtone()
            print("[i] -- Curando... - [i]")
            beep_ringtone()
            chance = random.randint(0,1)
            if chance == 1:
                print("[V] -- CURADO COM SUCESSO! -- [V]")
                self.saude == 100
                beep_ringtone_keep()
            else:
                print("[X] -- ERRO AO CURAR, SUA SAÚDE DIMINUIU. -- [X]")
                self.saude -= 15
                beep_critical()
        else:
            print("Você não esta doente!")

class Loja:
    inst = []
    def __init__(self):
        self.items = {}
        Loja.inst.append(self)

    def add_item(self, item, value, quantidade, classe, nutricao):
        self.items[item] = {"name":item, "value":value, "quantidade":quantidade, "classe":classe, "saturacao":nutricao}

    def remove_item(self, remitem):
        if self.items[remitem]:
            dict.pop(self.items, remitem)
    def list_items(self, player):
        beep_ringtone_fast()  
        print("\n [+]--- LOJA ---[+] \n")
        for _, item in self.items.items():
            item_name = item["name"]
            item_val = item["value"]
            item_q = item["quantidade"]
            print(f"{item_q}x de {item_name} por {item_val}\n")  
    def random_restock(self,min,max):
        for _, item in self.items.items():
            randomnum = random.randint(min, max)
            item["quantidade"] += randomnum
    def get_shops(self):
        print("[$] -- LOJAS -- [$] \n")
        id = 0
        for instance in self.inst:
            id += 1
            print(f"{id}: \n")
            instance.list_items()
if __name__ == "__main__":
    shop = Loja()

    shop.add_item("Batata", 50, 10, "comida", "mediana")

    shop.random_restock(1, 10)




    maria = Trabalhador("Maria", 18, 123, "Desempregado", 10000)

    shop.list_items(maria)


    maria.comprar_item(shop, "Batata", 2)
    maria.fome = 50
    maria.mostrar_armazenavel('geladeira')
    maria.comer()
    maria.mostrar_armazenavel("geladeira")
    maria.comer()




