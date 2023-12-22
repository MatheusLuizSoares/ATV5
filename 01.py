import requests,datetime,os, csv, json

strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)
strNomeArq = f'{strDiretorio}/relacao_servidores_ifrn.csv'

with open(strNomeArq, "r", encoding="UTF-8") as file:
    csv_reader=csv.reader(file)
    header=next(csv_reader)
    dictServidores = [list(zip(header, row)) for row in csv_reader]
listInfo=[]
listdoc=[]

for servidor in dictServidores:
    servidor_info=servidor[0][1].split(";")

    sigla_campos=servidor_info[11] if len(servidor_info)>=12 and servidor_info[11] and not servidor_info[11].isdigit()else None
    categoria=servidor[0][1].split(';')[0]

    if sigla_campos and not sigla_campos.isdigit():
        campos_encontrado=False
        for campus_entry in listInfo:
            if campus_entry[0]==sigla_campos:
                if categoria in campus_entry[1]:
                    campus_entry[1][categoria]+=1

                else:
                 campus_entry[1][categoria] = 1
                campus_encontrado = True
                break
            

        if not campus_encontrado:
            listInfo.append([sigla_campos, {'docente': 0, 'tecnico_administrativo': 0, 'estagiario': 0, 'indefinida': 0}])
            for campus_entry in listInfo:
                if campus_entry[0] == sigla_campos:
                    campus_entry[1][categoria] += 1
                    break


for servidor_info in dictServidores:

    if len(servidor_info[0][1].split(';')) >= 2 and servidor_info[0][1].split(';')[1]:
        disciplina_ingresso = servidor_info[0][1].split(';')[1]
        encontrado = False
        for item in listdoc:
            if item[0] == disciplina_ingresso:
                item[1] += 1
                encontrado = True
                break
        if not encontrado:
            listdoc.append([disciplina_ingresso, 1])

listdoc.sort(key=lambda x: x[0])

diretorio_script = os.path.dirname(os.path.abspath(__file__))

caminho_arquivo_csv = os.path.join(diretorio_script, "servidores_campi.csv")

with open(caminho_arquivo_csv, mode='w', newline='', encoding='UTF-8') as arquivo_csv:

    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    
    escritor_csv.writerow(["Sigla do Campus", "Docente", 'tecnico_administrativo', 'estagiario', 'indefinida'])
    
    for campus_entry in listInfo:
        escritor_csv.writerow([campus_entry[0], campus_entry[1]['docente'], campus_entry[1]['tecnico_administrativo'], campus_entry[1]['estagiario'], campus_entry[1]['indefinida']])

print(f"Os dados dos servidores foram salvos na pasta raiz.")


caminho_arquivo_csv = os.path.join(diretorio_script, "docentes_disciplinas.csv")
with open(caminho_arquivo_csv, mode='w', newline='', encoding='UTF-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    
    escritor_csv.writerow(['Disciplina', 'quantidade de docentes da disciplina'])
    
    for docente_entry in listdoc:
        escritor_csv.writerow([docente_entry[0], docente_entry[1]])

caminho_arquivo_csv_servidores = os.path.join(strDiretorio, "servidores_campi.csv")

with open(caminho_arquivo_csv_servidores, 'w', newline='', encoding='UTF-8') as arquivo_csv:

    arquivo_csv.write(" - ".join(["Sigla do Campus", "Docente", 'tecnico_administrativo', 'estagiario', 'indefinida']) + '\n')

    for campus_entry in listInfo:

        arquivo_csv.write(" - ".join([campus_entry[0], str(campus_entry[1]['docente']), str(campus_entry[1]['tecnico_administrativo']), str(campus_entry[1]['estagiario']), str(campus_entry[1]['indefinida'])]) + '\n')

print(f"Os dados dos servidores foram salvos em {caminho_arquivo_csv_servidores}.")

caminho_arquivo_csv_docentes = os.path.join(strDiretorio, "docentes_disciplinas.csv")


