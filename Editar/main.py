import random

def criarVetor(tam):
    vetor = [0] * tam
    for i in range(0, tam):
        vetor[i] = random.randint(0, 200)
    return vetor

def exibirVetor(x):
    for i in range(0, len(x)):
        print(x[i], end="|")
    print(" ")

def somarImpares(x):
    impares = 0
    for i in range(0, len(x)):
        if(x[i] % 2 == 1):
            impares += x[i]
    return impares

def busca(num, vet):
    for i in range(0, len(vet)):
        if(vet[i] == valor):
            print(f"O valor {num} esta no vetor")
            return True

    print(f"O valor {num} não esta no vetor")
    return False

valor = 0
def ordenar(v, tipo):
    if(tipo.lower() == "Bolha"):
        for ciclos in range(0, len(v)-1):
            for i in range(0, len(v)-1):
                if(v[i] > v[i+1]):
                    temp = v[i]
                    v[i] = v[i+1]
                    v[i+1] = temp

    if(tipo.lower() == "Inserção"):
        for i in range(1, len(v)):
            valor = v[i]
            i_ant = i - 1

            while(i_ant >= 0 and v[i_ant] > valor):
                v[i_ant+1] = v[i_ant]
                i_ant -= 1

            v[i_ant+1] = valor

    if(tipo.lower() == "Seleção"):
        for i in range(0, len(v)-1):
            menor = v[i]
            i_menor = i

            for j in range(i+1, len(v)):
                if(v[j] < menor):
                    menor = v[j]
                    i_menor = j

            temp = v[i]
            v[i] = menor
            v[i_menor] = temp

    return v
