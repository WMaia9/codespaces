class Fila:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.fila = []

    def enqueue(self, valor):
        if len(self.fila) < self.tamanho_maximo:
            self.fila.append(valor)

    def dequeue(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)

    def imprimir_fila(self):
        for valor in self.fila:
            print(valor, end=' ')


tamanho = int(input())
fila = Fila(tamanho)

entrada = input().split()

for i in range(0, len(entrada), 2):
    operacao = entrada[i]
    valor = int(entrada[i + 1])

    if operacao == 'i':
        fila.enqueue(valor)
    elif operacao == 'r':
        fila.dequeue()

fila.imprimir_fila()