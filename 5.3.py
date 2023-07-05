class Aluno:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


class Pilha:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.pilha = []

    def push(self, aluno):
        if len(self.pilha) < self.tamanho_maximo:
            self.pilha.append(aluno)

    def pop(self):
        if len(self.pilha) > 0:
            return self.pilha.pop()

    def imprimir_pilha(self):
        for aluno in self.pilha[::-1]:
            print(f"{aluno.nome} {aluno.idade} {aluno.sexo}", end="\t")


tamanho = int(input())
pilha = Pilha(tamanho)

entrada = input().split()

for i in range(0, len(entrada), 4):
    operacao = entrada[i]
    nome = entrada[i + 1]
    idade = entrada[i + 2]
    sexo = entrada[i + 3]

    if operacao == 'i':
        aluno = Aluno(nome, idade, sexo)
        pilha.push(aluno)
    elif operacao == 'r':
        pilha.pop()

pilha.imprimir_pilha()