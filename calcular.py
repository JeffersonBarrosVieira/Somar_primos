import PyPDF2 as py2
import numpy as np
import os
import time
import re

pdf = open("primos.pdf", "rb")
pdf_reader = py2.PdfFileReader(pdf)

n = pdf_reader.numPages


def removerSujeiras(pagina):
    page = pdf_reader.getPage(pagina)
    texto = page.extractText()

    sujeiras = ['\n', 'Até', 'Lista', 'de', 'Números', 'Primos', '10:', '100:', '1000:', '10000:', '100000:', '200000:', '300000:','400000:', '500000:', '600000:', '700000:', '800000:', '900000:', '1000000:', '1000000:']
    tamanho_sujeiras = int(len(sujeiras)) -1

    for i in range(0, tamanho_sujeiras):
        texto = re.sub(sujeiras[i], '', texto)

    for i in range(0, 10):
        texto = re.sub('  ', ' ', texto)
    
    return texto

def agruparPaginas(num):
    texto = removerSujeiras(0)
    for i in range(0, num -1):
        texto += removerSujeiras(i+1)

    return texto

def toArray(arquivo):
    texto = arquivo.split()
    texto = np.asarray(texto)

    return texto

def Somar(arr):
    meio = int(len(arr)/2)
    soma = []

    for i in range(0, meio):
        soma.append(str(int(arr[i]) + int(arr[(2*meio -1) - i])))
    return soma

def reduzirSoma(arr, num):

    while(len(arr) >num):
        arr = Somar(arr)
    return arr

def toInt(arr):
    for i in range(0, len(arr) -1):
        arr[i] = int(arr[i])
    return arr

def repetirSoma(arr, num):
    for i in range(0, num):
        arr = Somar(arr)

    return arr

def plotarGrafico(arr):
    import matplotlib.pyplot as plt

    r = np.arange(0, len(arr), 1)
    Y = arr

    plt.plot(r, Y)

    plt.yticks([])

    plt.show()

def escolherOpcao():
    while True:
        numero_de_paginas = int(input("Digite o Número de Páginas a ser somado: "))
        print("Aguarde...")
        texto = agruparPaginas(numero_de_paginas)
        texto = toArray(texto)
        soma = Somar(texto)
        soma = repetirSoma(soma, 0)
        soma = toInt(soma)

        time.sleep(1)

        os.system('clear')

        print("Escolha uma das opções abaixo: \n\n [1] - Imprimir as Somas dos números Primos; \n [2] - Plotar Gráfico das Somas. \n [3] - Finalizar Programa \n\n")
        opcao = int(input())

        if(opcao == 1):
            os.system('clear')
            print("Imprimindo...")
            time.sleep(1)
            os.system('clear')
            print(soma)
            print("\n")
        elif(opcao == 2):
            os.system('clear')
            print("Aguarde...")
            time.sleep(1)
            os.system('clear')
            plotarGrafico(soma)
        elif(opcao == 3):
            os.system('clear')
            print("Finalizando...")
            break
        else:
            print("Opcao escolhida não existe. \n")
    time.sleep(0.5)
    os.system('clear')
    print("Finalizado com sucesso!!")

if __name__ ==  '__main__':
    escolherOpcao() 