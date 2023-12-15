from datetime import datetime
import requests, datetime,os
strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += '@dataInicial=%2701-01-2021%27&@dataFinalCotacao=%2712-31-2021%27&$format=json'

dictCotacoes = requests.get(strURL).json()

Ano_atual = datetime.datetime.now().year