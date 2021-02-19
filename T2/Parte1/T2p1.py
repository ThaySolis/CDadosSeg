#coding: utf-8
#Prática 2 - parte 1
#Thayse Marques Solis
#Matrícula: 202000131775


import xmltodict
import os
import sys

#Esta função separa, em dois dicionários, as permissões comuns a todas as APKs e aquelas que são únicas de alguma APK 
def separarPermissoes(DictPermissoesPorAPK):
    #Este dicionário guarda as permissões comuns a todas as APKs
    DictPermsEmComum = {}
    #Este dicionário guarda as permissões únicas por APK
    DictPermsUnicasPorAPK = {}
    #Para cada APK no dicionário original
    for APK in DictPermissoesPorAPK:
        #Para cada permissão em cada APK no dicionário original
        for permissao in DictPermissoesPorAPK[APK]:
            #Se a permissão já for chave de DictPermsEmComum, adiciona o nome da APK ao final do vetor de valores
            if permissao in DictPermsEmComum:
                DictPermsEmComum[permissao].append(APK)
            #Senão, cria um par chave-valor com a permissão e a APK em questão
            else:
                DictPermsEmComum[permissao]=[APK]
                
    #De acordo com o que foi coletado no dicionário de permissões comuns, para cada permissão:              
    for permissao in DictPermsEmComum:
        #Se só houver um APK com a permissão
        if len(DictPermsEmComum[permissao])==1:
            #O APK é o campo [0] da lista
            APK = DictPermsEmComum[permissao][0]
            #Se o APK já for chave no dicionário de permissões únicas, só coloca a permissão na lista de valores
            if APK in DictPermsUnicasPorAPK:
                DictPermsUnicasPorAPK[APK].append(permissao)
            #Senão, aiciona a permissão na chave APK correspondente
            else:
                DictPermsUnicasPorAPK[APK]=[permissao]
    #Retorna os dois dicionários
    return (DictPermsEmComum, DictPermsUnicasPorAPK)
    

try:
    #diretorio recebe o diretório com as APKs de argv[1]
    diretorio = sys.argv[1]
    #Este dicionário guarda as permissões de cada APK
    DictPermissoesPorAPK={}
    #Itera por todos os arquivos presentes no diretório informado
    for filename in os.listdir(diretorio):
        #Cria o nome a ser exibido por APK a partir do filename (remove AndroidManifest_ e a extensão xml)
        apk_name = str(filename).replace("AndroidManifest_", "").replace(".xml", "")
        #Para cada chave "apk_name" o dicionário terá um conjunto de permissões armazenado em uma lista
        DictPermissoesPorAPK[apk_name]=[]
        #Abre os arquivos no modo leitura
        with open(os.path.join(diretorio, filename), 'r') as f:
            #O xml em análise é o conteúdo de cada arquivo
            my_xml = f.read()
            #Usa o parser da biblioteca xmltodict no arquivo xml
            my_dict = xmltodict.parse(my_xml)
            #Para cada permissão no dicionário, na tag "manifest" e dentro do tag "uses-permission"
            for perm in my_dict["manifest"]["uses-permission"]:
                #A permissão será o atributo "android:name" da permissão lida do xml, separada por "." e tomado o seu último campo
                permissao=perm["@android:name"].split(".")[-1]
                #adiciona a permissão ao final da lista correspondente a APK
                DictPermissoesPorAPK[apk_name].append(permissao)
    #Executa a função separarPermissoes e armazena os valores de retorno em duas variáveis       
    (DictPermsEmComum, DictPermsUnicasPorAPK)=separarPermissoes(DictPermissoesPorAPK)        
                        
    print("==========================\n" 
          "Permissões por APK\n"
          "==========================\n")
    #Para cada APK no dicionário DictPermissoesPorAPK, imprime o nome da APK e a lista de permissões (convertida para string)
    for APK in DictPermissoesPorAPK:
        print(APK + ": " + str(DictPermissoesPorAPK[APK]) + "\n")
            
    print("==========================\n"
          "Permissões únicas por APK\n"
          "==========================\n")
    #Para cada APK no dicionário DictPermsUnicasPorAPK, imprime o nome da APK e a lista de permissões únicas para a APK em questão (convertida para string)
    for APK in DictPermsUnicasPorAPK:
        print(APK + ": " + str(DictPermsUnicasPorAPK[APK]) + "\n")
    
    print("==========================\n"
          "Permissões comuns das APKs\n"
          "==========================\n")
    #Para cada permisão no dicionário DictPermsEmComum, se a permissão estiver em todos os APKs, imprime a permissão
    for permissao in DictPermsEmComum:
        if len(DictPermsEmComum[permissao])==len(DictPermissoesPorAPK):
            print(permissao + "\n")

except ValueError:
    print("Como invocar: python T2p1.py <diretório>")