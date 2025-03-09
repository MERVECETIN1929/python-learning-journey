class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def get_value(self):
        return self.val

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    # kuyruğun başındaki düğümün verisini döndermek

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("Görüntülenecek bir değer yok !")

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Kuyruğa " + str(item_to_add.get_value()) + " ekleniyor . . . ")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Kuyrukta yeterli alan yok !")
    # Düğüm kaldırma fonksiyonumuzu tanımlayalım

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print("Kuyruktan " + str(item_to_remove.get_value()) +
                  " kaldırılıyor . . . ")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Kuyruk boş ! ")

    # get_size(), has_space() ve is_empty() metotlarını tanımlayalım
    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0


# Bos bir pizza yığını tanımlayalım
pizza_stack = Queue(6)
# Sahip olduğumuz pizzaları yığına ekleyelim
pizza_stack.enqueue("pizza #1")
pizza_stack.enqueue("pizza #2")
pizza_stack.enqueue("pizza #3")
pizza_stack.enqueue("pizza #4")
pizza_stack.enqueue("pizza #5")
pizza_stack.enqueue("pizza #6")

# Limit değişkenine değer olarak 6 atadık fazla pizza eklemeye çalışırsak ne olacak görmek için aşağıdaki satırı yorumdan çıkarın.
# pizza_stack.push("pizza #7")

# Yığının tepesinden aşağı doğru pizzaları teslim edelim
print("İlk Teslim Edilen Pizza :  " + str(pizza_stack.peek()))
pizza_stack.dequeue()
pizza_stack.dequeue()
pizza_stack.dequeue()
pizza_stack.dequeue()
pizza_stack.dequeue()
pizza_stack.dequeue()

# Tüm pizzalar dağıtılmasına rağmen 'pop()' işlemi yaparsak ne olur görmek için aşağıdaki satırı yorumdan çıkarın.
print(str(pizza_stack.peek()))
