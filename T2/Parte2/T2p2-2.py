#coding: utf-8
#Prática 2 - Parte 2-2
#Thayse Marques Solis
#Matrícula: 202000131775

import pefile
import sys
import os

#Valores das flags Characteristics retiradas de https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_section_header
#Esta função verifica se a seção é executável
def isExecutable(section):
    #Salva em uma variável local a bitmask com características da seção
    characteristics = section.Characteristics
    #Se o bit 0x20000000 estiver setado, a seção é executável
    if (characteristics & 0x20000000) != 0:
        return True
    return False
    
#Esta função verifica se a seção pode ser lida
def isReadable(section):
    characteristics = section.Characteristics
    #Se o bit 0x40000000 estiver setado, a seção pode ser lida
    if (characteristics & 0x40000000) != 0:
        return True
    return False
    
#Esta função verifica se a seção pode ser escrita
def isWritable(section):
    characteristics = section.Characteristics
    #Se o bit 0x80000000 estiver setado, a seção pode ser escrita
    if (characteristics & 0x80000000) != 0:
        return True
    return False

try:
    #Primeiro arquivo binário, recebido por argv[1]
    binario1 = sys.argv[1]
    #Segundo arquivo binário, recebido por argv[2]
    binario2 = sys.argv[2]
    #Lista de arquivos
    arquivos = [binario1, binario2]
    #Dicionário com as seções dos arquivos
    DicSecoes = {}
    #Contador de arquivos
    count = 0
    #Para cada arquivo de entrada
    for filename in arquivos:
        #Incrementa o contador de arquivos
        count+=1
        #Salva o nome do arquivo sem o caminho completo em uma variável
        nome_arquivo = os.path.basename(filename)
        #Processa o PE e extrai as seções
        pe =  pefile.PE(filename)
        #Para cada seção no arquivo
        for section in pe.sections:
            #Converte o nome da seção que está em bytes para string, tirando caracteres desnecessários
            secao = section.Name.decode('utf-8').replace("\x00","")
            #Se a seção já estiver no dicionário, adiciona o nome do arquivo atual na lista de arquivos com a seção atual
            if secao in DicSecoes:
                DicSecoes[secao].append(nome_arquivo)
            #Se a seção ainda não estiver no dicionário, adiciona e cria uma lista contendo o nome do arquivo atual
            else:
                DicSecoes[secao]=[nome_arquivo]
            
    print("===========================================================\n"
          "Seções comuns\n"
          "===========================================================\n")
    #Para cada seção no dicionário
    for secao in DicSecoes:
        #Se ela estiver em todos os arquivos, imprime seu nome
        if len(DicSecoes[secao])==count:
            print(secao + "\n")
      
    print("===========================================================\n"
          "Seções presentes apenas em " + os.path.basename(binario1) + "\n"
          "===========================================================\n")
    #Para cada seção no dicionário
    for secao in DicSecoes:
        #Se ela estiver em apenas um arquivo e o nome do arquivo é o do primeiro binário, imprime
        if len(DicSecoes[secao])==1 and DicSecoes[secao][0] == os.path.basename(binario1):
            print(secao + "\n")
    
    print("===========================================================\n"
          "Seções presentes apenas em " + os.path.basename(binario2) + "\n"
          "===========================================================\n")
    #Para cada seção no dicionário
    for secao in DicSecoes:
        #Se ela estiver em apenas um arquivo e o nome do arquivo é o do segundo binário, imprime
        if len(DicSecoes[secao])==1 and DicSecoes[secao][0] == os.path.basename(binario2):
            print(secao + "\n")

except ValueError:
    print("Como invocar: python T2p2-2.py <binario1> <binario2>")