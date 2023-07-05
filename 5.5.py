class Carro:
    def __init__(self, nome, ano, valor):
        self.nome = nome
        self.ano = ano
        self.valor = valor


class Fila:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.fila = []

    def enqueue(self, carro):
        if len(self.fila) < self.tamanho_maximo:
            self.fila.append(carro)

    def dequeue(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)

    def imprimir_fila(self):
        for carro in self.fila:
            print(f"{carro.nome} {carro.ano} {carro.valor:.2f}")


tamanho = int(input())
fila = Fila(tamanho)

operacoes = input().split()

for i in range(0, len(operacoes), 4):
    operacao = operacoes[i]
    if operacao == 'i':
        nome = operacoes[i + 1]
        ano = int(operacoes[i + 2])
        valor = float(operacoes[i + 3])
        carro = Carro(nome, ano, valor)
        fila.enqueue(carro)
    elif operacao == 'r':
        fila.dequeue()

fila.imprimir_fila()