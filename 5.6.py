def insert_with_linked_list(N, M, elements):
    hash_table = [[] for _ in range(N)]
    for element in elements:
        index = element % N
        hash_table[index].append(element)
    return hash_table


def insert_with_linear_probing(N, M, elements):
    hash_table = [None] * N
    for element in elements:
        index = element % N
        while hash_table[index] is not None:
            index = (index + 1) % N
        hash_table[index] = element
    return hash_table


def print_hash_table(hash_table):
    for index, entry in enumerate(hash_table):
        if len(entry) > 0:
            print(f'[{index}] -> {", ".join(map(str, entry))}')
        else:
            print(f'[{index}] ->')


# Leitura da entrada
approach = int(input())
N, M = map(int, input().split())
elements = list(map(int, input().split()))

if approach == 0:
    hash_table = insert_with_linked_list(N, M, elements)
else:
    hash_table = insert_with_linear_probing(N, M, elements)

# Imprime a tabela hash
print_hash_table(hash_table)