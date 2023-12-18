import requests,datetime, os, sys, json
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
            break

escalações = ["343", "352", "433", "442", "451", "532", "541"]
while True:
 escala_usuario =int( input("Escolha uma escalação ou digite 0 para sair: ").replace(".", "").replace(",", "").replace("","").replace("-",""))
 quantidade_jogadores_por_posicao = {
    'G': 1,
    'Z': 3,
    'L': 3 if '5' in escala_usuario else 4,
    'M': int(escala_usuario.split('-')[1]),
    'A': int(escala_usuario.split('-')[2]),
    'T': 1
   }

 if escala_usuario == "0":
        print("O programa foi finalizado.")
        sys.exit()

 elif escala_usuario not in escalações:
        print("Escalação inválida. Escolha uma das opções válidas.")
 else:
        break
dic_Atletas = {atleta: dic_cartola["atleta"] for atleta in range(len(dic_cartola["atletas"]))}