class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class TabelaHashListaEncadeada:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def inserir(self, valor):
        posicao = valor % self.tamanho

        if self.tabela[posicao] is None:
            self.tabela[posicao] = No(valor)
        else:
            novo_no = No(valor)
            novo_no.proximo = self.tabela[posicao]
            self.tabela[posicao] = novo_no

    def imprimir_tabela(self):
        for i, no in enumerate(self.tabela):
            elementos = []
            while no:
                elementos.append(str(no.valor))
                no = no.proximo
            print(f"[{i}] -> {' '.join(elementos)}" if elementos else f"[{i}] ->")


class TabelaHashSondagemLinear:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def inserir(self, valor):
        posicao = valor % self.tamanho

        while self.tabela[posicao] is not None:
            posicao = (posicao + 1) % self.tamanho

        self.tabela[posicao] = valor

    def imprimir_tabela(self):
        for i, valor in enumerate(self.tabela):
            print(f"[{i}] -> {valor}" if valor is not None else f"[{i}] ->")


abordagem = int(input())
tamanho, num_elementos = map(int, input().split())
elementos = list(map(int, input().split()))

if abordagem == 0:
    tabela = TabelaHashListaEncadeada(tamanho)
else:
    tabela = TabelaHashSondagemLinear(tamanho)

for elemento in elementos:
    tabela.inserir(elemento)

tabela.imprimir_tabela()