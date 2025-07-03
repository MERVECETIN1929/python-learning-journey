# queues veri yapısı kuyruk şeklinde verileri işlememize olanak tanır. bağlı liste mantığını kullanarak kodlayacağım.
# fonksiyonları:
# enqueue: kuyruğa veri eklemesine olanak tanır
# dequeue: kuyruktan eleman siler
# peek: kuyruğun başındaki elemanın değerini dönderir
# is_empty: kuyruğun boş olup olmadığını döner
# size: kuyruk boyutunu döner
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.q_size = 0
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.q_size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return_node = self.head
        self.head = self.head.next

        if self.q_size == 1:
            self.tail = self.head

        self.q_size -= 1
        return return_node.value

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.value

    def is_empty(self):
        return not self.q_size

    def size(self):
        return self.q_size

    def print_queue(self):
        head_node = self.head
        while head_node:
            print(head_node.value)
            head_node = head_node.next


queue = Queue()
print(queue.dequeue())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.print_queue()
print("ilk eleman:", queue.peek())
print("hizmet aldı:", queue.dequeue())
print("hizmet aldı:", queue.dequeue())
print("hizmet aldı:", queue.dequeue())
print("hizmet aldı:", queue.dequeue())
queue.print_queue()
print("kuyrukta bekleyen:", queue.size(), " kişi var.")
