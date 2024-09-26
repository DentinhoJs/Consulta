import os
import time
import json
import requests

# Cores
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[1;34m"
Y = "\033[1;33m"
r = "\033[0m"
n = "\033[1m"

# Logo do Deadpool
logo = """
  _______
 /      \\
|  Deadpool  |
 _______/
"""

# Função para limpar a tela
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para imprimir o menu
def menu():
    cls()
    print(logo)
    print(" ╭" + "─" * 40 + "╮")
    print(" │" + "  Menu  ".center(40) + "│")
    print(" ╞" + "═" * 40 + "╡")
    print(" │ 1. Localizar IP")
    print(" │ 2. Localizar DDD")
    print(" │ 3. Consultar CNPJ")
    print(" │ 4. Localizar CEP")
    print(" │ 5. Consultar WhoIS")
    print(" │ 6. Verificar Telefone")
    print(" │ 7. Consultar Clima")
    print(" │ 8. Consultar Notícias")
    print(" │ 99. Api's usadas")
    print(" │ 0. Sair")
    print(" ├" + "─" * 40 + "╯")

# Função para imprimir as opções
def print_options(options):
    for i, option in enumerate(options):
        print(f" │ {i+1}. {option}")

# Função para imprimir as informações
def print_info(info):
    for key, value in info.items():
        print(f" │ {key}: {value}")

# Função para consultar a API
def consult_api(url, headers=None):
    response = requests.get(url, headers=headers)
    return response.json()

# Função para imprimir as informações da API
def print_api_info(info):
    for key, value in info.items():
        print(f" │ {key}: {value}")

# Função para consultar o clima
def consult_clima():
    cidade = input(f"{Y}Digite a cidade que deseja consultar o clima: {r}")
    info = consult_api(f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=SEU_API_KEY")
    print_api_info(info)

# Função para consultar as notícias
def consult_noticias():
    categoria = input(f"{Y}Digite a categoria de notícias que deseja consultar (ex: tecnologia, política, etc.): {r}")
    info = consult_api(f"https://newsapi.org/v2/top-headlines?category={categoria}&country=br&apiKey=SEU_API_KEY")
    print_api_info(info)

# Inicializar o painel
def main():
    while True:
        menu()
        ipt = input(f" ├({R}Número da opção{r}) ")
        cls()
        try:
            ipt = int(ipt)
            if ipt not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 99]:
                cls()
                print(f"{R}Escolha uma opção válida{r}")
                time.sleep(2)
                cls()
                except:
            cls()
            print(f"{R}Escolha uma opção válida{r}")
            time.sleep(2)
            cls()
        match ipt:
            case 1:
                # Consultar IP
                ip = input(f"{Y}Digite o IP que deseja localizar: {r}")
                info = consult_api(f"http://ip-api.com/json/{ip}")
                print_api_info(info)
            case 2:
                # Consultar DDD
                ddd = input(f"{Y}Digite o DDD que deseja consultar: {r}")
                info = consult_api(f"https://brasilapi.com.br/api/ddd/v1/{ddd}")
                print_api_info(info)
            case 3:
                # Consultar CNPJ
                cnpj = input(f"{Y}Digite o CNPJ que deseja consultar: {r}")
                info = consult_api(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")
                print_api_info(info)
            case 4:
                # Localizar CEP
                cep = input(f"{Y}Digite o CEP que deseja localizar: {r}")
                info = consult_api(f"https://cep.awesomeapi.com.br/json/{cep}")
                print_api_info(info)
            case 5:
                # Consultar WhoIS
                dominio = input(f"{Y}Digite o domínio que deseja consultar: {r}")
                info = consult_api(f"https://api.apilayer.com/whois/query?domain={dominio}", headers={"apikey": "SEU_API_KEY"})
                print_api_info(info)
            case 6:
                # Verificar Telefone
                telefone = input(f"{Y}Digite o telefone que deseja verificar: {r}")
                info = consult_api(f"https://phonevalidation.abstractapi.com/v1/?api_key=SEU_API_KEY&phone={telefone}")
                print_api_info(info)
            case 7:
                # Consultar Clima
                consult_clima()
            case 8:
                # Consultar Notícias
                consult_noticias()
            case 99:
                # Api's usadas
                apis_usadas = {
                    "IP": "ip-api.com",
                    "DDD": "brasilapi.com.br",
                    "CNPJ": "brasilapi.com.br",
                    "CEP": "cep.awesomeapi.com.br",
                    "WhoIS": "apilayer.com",
                    "Verificação de telefone": "phonevalidation.abstractapi.com",
                    "Clima": "openweathermap.org",
                    "Notícias": "newsapi.org"
                }
                print_api_info(apis_usadas)
            case 0:
                # Sair
                print(f"{R}Obrigado por usar!{r}")
                break
            case _:
                print(f"{R}Escolha uma opção válida{r}")

if __name__ == "__main__":
    main()
