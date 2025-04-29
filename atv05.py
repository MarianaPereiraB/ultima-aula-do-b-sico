#escreva um código que permita a leitura das notas de uma turma de cinco alunos e guarde num vetor,
#calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada
#e escrever a média da turma e o resultado da contagem


nota = [""]*5
soma = 0
contador = 0
for l in range(5):
    nota[l] = float(input("digite a nota: "))
for m in range (5):
    soma = soma + nota[m]
media = soma/5
for o in range(5):
    if nota[o]>media:
        contador=contador+1
print(f"{contador} notas são maiores que a média{media}")