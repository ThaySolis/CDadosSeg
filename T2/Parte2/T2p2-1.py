#coding: utf-8
#Prática 3
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
    #diretorio recebe o diretório com as APKs de argv[1]
    diretorio = sys.argv[1]
    #Dicionário que irá armazenar as seções executaveis em uma lista, para cada binário
    dictSecoesExecutaveis={}
    #Para cada arquivo no diretório
    for filename in os.listdir(diretorio):
        #Processa o PE e extrai as seções
        pe =  pefile.PE(str(diretorio) + "/" + str(filename))
        #Para cada arquivo, cria uma lista que irá armazenar as seções executáveis
        dictSecoesExecutaveis[filename]=[]    
        #Para cada seção do arquivo
        for section in pe.sections:
            #Converte o nome da seção que está em bytes para string, tirando caracteres desnecessários
            secao = section.Name.decode('utf-8').replace("\x00","")
            #Se a seção for executável, adiciona na lista relativa ao PE atual
            if isExecutable(section):
                dictSecoesExecutaveis[filename].append(secao)

    print("===============================\n"
          "Seções executáveis por binários\n"
          "===============================\n")
    #Para cada arquivo no dicionário, imprime o nome do arquivo e a lista de suas seções executáveis (convertida para string)
    for filename in dictSecoesExecutaveis:
        print(filename + ": " + str(dictSecoesExecutaveis[filename]) + "\n")
except ValueError:
    print("Como invocar: python T2p2-1.py <diretório>")

