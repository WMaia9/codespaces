class Node:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_ordered(self, age, name):
        new_node = Node(age, name)

        if self.head is None or age < self.head.age:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and age >= current.next.age:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.name)
            current = current.next


# Função principal
def main():
    n = int(input())

    linked_list = LinkedList()

    for _ in range(n):
        age, name = input().split(' ', 1)
        linked_list.insert_ordered(int(age), name)

    linked_list.print_list()


if __name__ == '__main__':
    main()