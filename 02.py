import requests
import datetime
import os
import sys
import json

strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)
Ano_atual = datetime.datetime.now().year
while True:
    ano = int(input("Escolha um ano ou digite 0 para sair:"))
    
    if ano == 0:
        print("Você está saindo do programa")
        sys.exit()
    
    if ano > Ano_atual:
        break
    elif ano == Ano_atual:
        dic_cartola = requests.get(strURL, verify=True).json()
        break
    else:
     strNomeArq = f"{strDiretorio}/cartola_fc_{ano}.json"
    with open(strNomeArq, "r", encoding='UTF-8') as dictOpen:
        dic_cartola = json.load(dictOpen)
  