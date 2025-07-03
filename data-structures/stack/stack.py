# linked list veri yapısını kullanarak stack yazmak
# fonksiyonlar:
# push : eleman ekleme
# pop: son elemenı geri dönder ve sil
# peek: son elemanın değerini geri dönder
# size: eleman boyutunu geri dönder
# isEmpty: yapının boş olma durumunu kontrol et
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.stack_size = 0

    def push(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.stack_size += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        return_node = self.head
        self.head = self.head.next
        self.stack_size -= 1
        return return_node.value

    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        return self.head.value

    def is_empty(self):
        return not self.stack_size

    def size(self):
        return self.stack_size

    def print_stack(self):
        head_node = self.head
        while head_node:
            print(head_node.value)
            head_node = head_node.next


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
print("eleman ekleme sonrası")
stack.print_stack()
print("son eleman: ", stack.peek())
print(stack.pop())
print("eleman silme sonrası")
stack.print_stack()
print("eleman boyutu:", stack.size())
