class Pilha:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.pilha = []

    def push(self, valor):
        if len(self.pilha) < self.tamanho_maximo:
            self.pilha.append(valor)

    def pop(self):
        if len(self.pilha) > 0:
            return self.pilha.pop()

    def obter_pilha(self):
        return self.pilha[::-1]


tamanho = int(input())
pilha = Pilha(tamanho)

operacoes = input().split()

for i in range(0, len(operacoes), 2):
    operacao = operacoes[i]
    valor = int(operacoes[i + 1])

    if operacao == 'i':
        pilha.push(valor)
    elif operacao == 'r':
        pilha.pop()

resultado = pilha.obter_pilha()
print(' '.join(map(str, resultado)))