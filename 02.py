import requests, datetime, os
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
Ano_atual = datetime.datetime.now().year

while True:
    ano=(int("Escolha um ano até 2021>="))
    if ano>Ano_atual:
     break
if ano==Ano_atual:
    dic_cartolA=requests.get(strURL, verify=False).json()


esquemas = ('343','352','433','442','451','532','541')