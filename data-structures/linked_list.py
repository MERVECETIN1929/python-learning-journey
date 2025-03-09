class Node:
    # yapıcı metottur. düğüm oluşturulurken değerini ve referans düğümünü ayarlar.
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    # düğümün verisini geri dönderir
    def get_value(self):
        return self.val

    # düğümün referans ettiği düğümü geri dönderir
    def get_next_node(self):
        return self.next_node

    # düğümün referans düğümünü ayarlar
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, val):
        self.head_node = Node(val)

    def get_head_node(self):
        return self.head_node

    def insert_begining(self, new_val):
        new_node = Node(new_val, self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_data = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_data += str(current_node.get_value())+"\n"
                current_node = current_node.get_next_node()
        return string_data

    def remove_node(self, value_to_remove):
        self.value_to_remove = value_to_remove
        current_node = self.get_head_node()
        if current_node.get_value() == self.value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node and current_node.get_next_node():
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    break
                else:
                    current_node = next_node


li = LinkedList(5)
li.insert_begining(70)
li.insert_begining(1231)
li.insert_begining(87)
li.remove_node(70)
print(li.stringify_list())
