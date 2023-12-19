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
            dic_cartola=json.loads(dic_cartola)
            dictOpen.close()
            break

clubes = dic_cartola.get('clubes')
clubes_dic = {}
for id_clube, info_clube in clubes.items():
    nome_clube = info_clube['nome']
    clubes_dic[id_clube] = nome_clube
atletas = dic_cartola.get('atletas')
maiores_pontuacoes={}
posicoes = {1: 'goleiro', 2: 'lateral', 3: 'zagueiro', 4: 'meia', 5: 'atacante', 6: 'tecnico'}


for atleta in atletas:
    nome = atleta['nome']
    apelido = atleta['apelido']
    clube_id = atleta['clube_id']
    clube = clubes_dic[str(clube_id)]
    posicao_id = atleta['posicao_id']
    jogos_num = atleta['jogos_num']
    media_num = atleta['media_num']
    maior_pontuacao = round(jogos_num * media_num, 2)
    maiores_pontuacoes[nome] = {'pontuacao': maior_pontuacao, 'posicao': posicoes[posicao_id], 'apelido' : apelido, 'clube': clube}
melhores_atletas = sorted(maiores_pontuacoes.items(), key=lambda x: x[1]['pontuacao'], reverse=True)
maiores_pontuacoes={}
melhores_goleiros = {}
melhores_laterais = {}
melhores_zagueiros = {}
melhores_meias = {}
melhores_atacantes = {}
melhores_tecnicos = {}
maiores_pontuacoes[nome] = {'pontuacao': maior_pontuacao, 'posicao': posicoes[posicao_id], 'apelido' : apelido, 'clube': clube}

escalações = ["343", "352", "433", "442", "451", "532", "541"]
for jogador,info in melhores_atletas:
    posicao=info("posição")
escala_usuario =int( input("Escolha uma escalação ou digite 0 para sair: ").replace(".", "").replace(",", "").replace("","").replace("-",""))
if posicao == 'goleiro':
        melhores_goleiros[jogador] = info
elif posicao == 'lateral':
        melhores_laterais[jogador] = info
elif posicao == 'zagueiro':
        melhores_zagueiros[jogador] = info
elif posicao == 'meia':
        melhores_meias[jogador] = info
elif posicao == 'atacante':
        melhores_atacantes[jogador] = info
elif posicao == 'tecnico':
        melhores_tecnicos[jogador] = info

if escala_usuario == "0":
        print("O programa foi finalizado.")
        sys.exit()

elif escala_usuario not in escalações:
        print("Escalação inválida. Escolha uma das opções válidas.")
else:
  dic_Atletas = {atleta: dic_cartola["atleta"] for atleta in range(len(dic_cartola["atletas"]))}


  maiores_pontuacoes[nome] = {'pontuacao': maior_pontuacao, 'posicao': posicoes[posicao_id], 'apelido' : apelido, 'clube': clube}

  melhores_atletas = sorted(maiores_pontuacoes.items(), key=lambda x: x[1]['pontuacao'], reverse=True)