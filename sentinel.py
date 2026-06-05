import os
import json

# Função para garantir a existência da pasta de dados
def garantir_pasta_alvos():
    if not os.path.exists("alvos"):
        os.makedirs("alvos")

# Chamada para garantir o ambiente logo ao iniciar
garantir_pasta_alvos()

def banner():
    os.system('clear')
    print("\033[1;31m")
    print(" ██████╗ ███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗     ")
    print("██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     ")
    print("╚█████╗  █████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     ")
    print(" ╚═══██╗ ██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║     ")
    print("██████╔╝ ███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗")
    print("╚═════╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝")
    print("          [ CENTRAL OPERATIONAL SYSTEM - V2.3 ]")
    print("\033[0m")

def cadastrar():
    banner()
    codinome = input("Codinome do Alvo: ").strip().upper()
    pasta = f"alvos/{codinome}"
    if not os.path.exists(pasta): os.makedirs(pasta)
    
    dados = {
        "Nome Completo": input("Nome Completo: "),
        "Nascimento": input("Data de Nascimento: "),
        "CPF": input("CPF: "),
        "RG": input("RG: "),
        "RA": input("RA: "),
        "Nome do Pai": input("Nome do Pai: "),
        "Nome da Mãe": input("Nome da Mãe: "),
        "CPF Parental (Mãe)": input("CPF da Mãe: "),
        "RG Parental (Mãe)": input("RG da Mãe: "),
        "Telefone Mãe": input("Telefone da Mãe: "),
        "Endereço": input("Endereço: "),
        "Status": "REGULAR"
    }
    
    with open(f"{pasta}/data.json", "w", encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print(f"\n\033[1;32m[V] Dossiê {codinome} atualizado!\033[0m")
    input("\nEnter para voltar...")

def listar():
    banner()
    if not os.listdir("alvos"):
        print("Banco de dados vazio."); input("\nEnter..."); return
    print("[+] Alvos Registrados:")
    for p in os.listdir("alvos"): print(f" -> {p}")
    escolha = input("\nDigite o Codinome: ").strip().upper()
    caminho = f"alvos/{escolha}/data.json"
    if os.path.exists(caminho):
        banner()
        print(f"\033[1;33m--- EXIBINDO DOSSIÊ: {escolha} ---\033[0m\n")
        with open(caminho, "r", encoding='utf-8') as f:
            d = json.load(f)
            for k, v in d.items(): print(f"\033[1;36m{k}:\033[0m {v}")
        input("\n[Enter] para voltar...")
    else:
        print("Erro: Dossiê não encontrado."); input("\nEnter...")

def editar():
    banner()
    if not os.listdir("alvos"):
        print("Banco de dados vazio."); input("\nEnter..."); return
    
    print("[+] Selecione o Alvo para editar:")
    for p in os.listdir("alvos"): print(f" -> {p}")
    
    escolha = input("\nCodinome para editar: ").strip().upper()
    caminho = f"alvos/{escolha}/data.json"
    
    if os.path.exists(caminho):
        with open(caminho, "r", encoding='utf-8') as f:
            dados = json.load(f)
        
        banner()
        print(f"\033[1;33m--- EDITANDO: {escolha} ---\033[0m")
        print("Deixe em branco para manter o valor atual.\n")
        
        for chave in dados.keys():
            novo_valor = input(f"\033[1;36m{chave}\033[0m [{dados[chave]}]: ").strip()
            if novo_valor != "":
                dados[chave] = novo_valor
        
        with open(caminho, "w", encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"\n\033[1;32m[V] Dados de {escolha} atualizados com sucesso!\033[0m")
    else:
        print("\033[1;31mErro: Alvo não encontrado.\033[0m")
    input("\nEnter para voltar...")

while True:
    banner()
    print("1. Cadastrar/Atualizar Alvo")
    print("2. Acessar Banco de Dados")
    print("3. Sair")
    print("4. Editar Dados")
    op = input("\nSENTINEL > ")
    if op == '1': cadastrar()
    elif op == '2': listar()
    elif op == '3': break
    elif op == '4': editar()
