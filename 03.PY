import requests
import os
import json
from datetime import datetime

strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += '@dataInicial=%2701-01-2021%27&@dataFinalCotacao=%2712-31-2021%27&$format=json'
dictCotacoes = requests.get(strURL).json()

Ano_atual = datetime.datetime.now().year
while True:
 ano=int(input("Digite um ano qualquer (que não seja superior ao ano atual):"))
 if ano>Ano_atual:
  break

while True:
    try:
        Ano_atual = datetime.now().year
        ano = int(input("Escolha um ano: "))
        
        if ano > Ano_atual:
            print("Digite um valor menor válido.")
            continue
        break 
    except ValueError:
        print("\nERROR: O valor informado precisa ser inteiro de base 10!")
        continue

dicDados = {}
mediasMes = {}

for cotacao in dictCotacoes["value"]:
    dataCotacao = cotacao["dataHoraCotacao"].split("T")[0]
    mes = dataCotacao.split("-")[1]
    compra = cotacao["cotacaoCompra"]
    venda = cotacao["cotacaoVenda"]
    
    if mes not in mediasMes:
        mediasMes[mes] = {"soma_compra": compra, "soma_venda": venda, "contador": 1}
    else:
        mediasMes[mes]['soma_compra'] += compra
        mediasMes[mes]['soma_venda'] += venda
        mediasMes[mes]['contador'] += 1

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

for mes in list(mediasMes.keys()):
    mesNumero = int(mes)
    mesNome = meses[mesNumero]
    dicDados[mesNome] = mediasMes[mes]

diretorio = os.path.dirname(os.path.abspath(__file__))
caminhoArquivoJSON = os.path.join(diretorio, f"medias_cotacoes_{ano}.json")

with open(caminhoArquivoJSON, 'w', encoding='utf-8') as arquivoJson:
    json.dump(dicDados, arquivoJson, ensure_ascii=False, indent=2)

caminhoArquivoCSV = os.path.join(diretorio, f"medias_cotacoes_{ano}.csv")

with open(caminhoArquivoCSV, mode='w', encoding='UTF-8') as arquivoCSV:
    arquivoCSV.write("mes - media_compra - media_venda\n")

    for mes, medias in dicDados.items():
        mediaCompra = f"{medias['soma_compra'] / medias['contador']:.5f}"
        mediaVenda = f"{medias['soma_venda'] / medias['contador']:.5f}"
        arquivoCSV.write(f"{mes} - {mediaCompra} - {mediaVenda}\n")

print(f"Os arquivos JSON e CSV foram salvos no diretório: {diretorio}.")

