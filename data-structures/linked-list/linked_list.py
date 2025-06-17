class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node_value):
        self.head_node = Node(head_node_value)

    def append(self, value):
        new_node = Node(value)
        current_node = self.head_node
        while current_node.next_node != None:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def printList(self):
        current_node = self.head_node
        while current_node:
            print(current_node.val)
            current_node = current_node.next_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next_node = self.head_node
        self.head_node = new_node

    def length(self):
        count = 0
        current_node = self.head_node
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count

    def search(self, value):
        current_node = self.head_node
        while current_node:
            if current_node.val == value:
                return True
            current_node = current_node.next_node

        return False

    def insertAfter(self, node, value):
        current_node = self.head_node
        new_node = Node(value)
        while current_node != node:
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def deleteByValue(self, value):
        current_node = self.head_node
        while current_node.next_node.val != value:
            current_node = current_node.next_node
        deleted_node = current_node.next_node
        current_node.next_node = deleted_node.next_node
        deleted_node.next_node = None

    def deleteByNode(self, node):
        current_node = self.head_node
        while current_node.next_node != node:
            current_node = current_node.next_node
        deleted_node = current_node.next_node
        current_node.next_node = deleted_node.next_node
        deleted_node.next_node = None

    def turn_node_byValue(self, value):
        current_node = self.head_node
        while current_node and current_node.val != value:
            current_node = current_node.next_node
        if not current_node:
            raise Exception("Sorry, no numbers in the linked list")
        return current_node

    def reverse(self):
        if not self.head_node:
            return self.head_node
        old_head_node = self.head_node
        current_node = Node(old_head_node.val)

        while old_head_node.next_node:
            old_head_node = old_head_node.next_node
            new_node = Node(old_head_node.val)

            new_node.next_node = current_node
            current_node = new_node
        self.head_node = current_node
        return self.head_node


linked_list = LinkedList(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.prepend(0)
linked_list.insertAfter(linked_list.turn_node_byValue(30), 50)
linked_list.printList()
print("--------------------")
linked_list.deleteByNode(linked_list.turn_node_byValue(50))
linked_list.printList()
print("linked list boyutu:  ", linked_list.length())
print(linked_list.search(10))
linked_list.printList()
deneme = linked_list.reverse()
print("liste ters")
while deneme:
    print(deneme.val)
    deneme = deneme.next_node

linked_list.printList()
