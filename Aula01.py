print("Bem-vindo ao sistema de cadastro de aluno")
nome = input("Qual o nome do aluno? ")
idade = int(input("Qual a idade do aluno? "))
peso = float(input("Qual o peso do aluno? "))
ativo = input("O Aluno está ativo? ")
if ativo == "Ativo" or ativo == "ativo" or ativo == "sim" or ativo == "Sim" or ativo == "True" or ativo == "true":
    ativo = True
elif ativo == "Inativo" or ativo == "inativo" or ativo == "não" or ativo == "Não" or ativo == "False" or ativo == "false":
    ativo = False
else:
    print("Valor incorreto na variavel ativo!")
    ativo = False
if ativo:
    print("O Aluno: " + nome + " está matriculado!")
else:
    print("O Aluno: " + nome + " não está matriculado!")

if idade < 18:
    print("O Aluno: " + nome + " é menor de idade!")
elif idade >= 18 and idade < 30:
    print("O Aluno: " + nome + " é jovem!")
else:
    print("O Aluno: " + nome + " é idoso!")