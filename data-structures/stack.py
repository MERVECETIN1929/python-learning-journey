class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.val


class Stack:
    def __init__(self,  limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def peek(self):
        if self.top_item.get_value() != None:
            return self.top_item.get_value()

    def pop(self):
        if not self.is_empty():
            remove_item = self.peek()
            self.top_item = self.top_item.get_next_node()
            self.size -= 1
            return remove_item
        else:
            print("Yığın tamamen boş.")

    def push(self, val):
        if self.has_space():
            buffer_node = Node(val)
            buffer_node.set_next_node(self.top_item)
            self.top_item = buffer_node
            self.size += 1
        else:
            print("yığın tamamen dolu.")

    def is_empty(self):
        if self.top_item == None:
            return True
        else:
            return False

    def has_space(self):
        if self.size < self.limit:
            return True
        else:
            return False


# Bos bir pizza yığını tanımlayalım
pizza_stack = Stack(6)
# Sahip olduğumuz pizzaları yığına ekleyelim
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Limit değişkenine değer olarak 6 atadık fazla pizza eklemeye çalışırsak ne olacak görmek için aşağıdaki satırı yorumdan çıkarın.
# pizza_stack.push("pizza #7")

# Yığının tepesinden aşağı doğru pizzaları teslim edelim
print("İlk Teslim Edilen Pizza :  " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
