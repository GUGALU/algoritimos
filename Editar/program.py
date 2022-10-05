import main

tam = int(input("Digite o tamanho do vetor: "))
vet1 = main.criarVetor(tam)
vet2 = main.criarVetor(tam)
vet3 = main.criarVetor(tam)

print("Vetor 1:")
main.exibirVetor(vet1)
print("Vetor 2:")
main.exibirVetor(vet2)
print("Vetor 3:")
main.exibirVetor(vet3)

s1 = main.somarImpares(vet1)
print("Soma do valores impares do vetor1 - ", s1)
s2 = main.somarImpares(vet2)
print("Soma do valores impares do vetor2 - ", s2)
s3 = main.somarImpares(vet3)
print("Soma do valores impares do vetor3 - ", s2)

n = int(input("Valor que deseja buscar no vetor1: "))
main.busca(n,vet1)

n = int(input("Valor que deseja buscar no vetor2: "))
main.busca(n, vet2)

n = int(input("Valor que deseja buscar no vetor3: "))
main.busca(n, vet3)

ordena = input("Digite o tipo de ordenação desejada para o vetor1: ")
vet1 = main.ordenar(vet1, ordena)
ordena = input("Digite o tipo de ordenação desejada para o vetor2: ")
vet2 = main.ordenar(vet2, ordena)
ordena = input("Digite o tipo de ordenação desejada para o vetor3: ")
vet3 = main.ordenar(vet3, ordena)
