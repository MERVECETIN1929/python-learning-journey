import sys


class Solution:
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()

    def pushCharacter(self, val):
        self.stack.pushCharacter(val)

    def popCharacter(self):
        return self.stack.popCharacter()

    def dequeueCharacter(self):
        return self.queue.dequeueCharacter()

    def enqueueCharacter(self, val):
        self.queue.enqueueCharacter(val)


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

# yığın


class Stack:
    def __init__(self):
        self.head_node = None

    def pushCharacter(self, val):
        if self.head_node == None:
            self.head_node = Node(val)
        else:
            buffer_node = Node(val)
            buffer_node.set_next_node(self.head_node)
            self.head_node = buffer_node

    def popCharacter(self):
        if self.head_node:
            buffer_node = self.head_node
            self.head_node = self.head_node.get_next_node()
            return buffer_node.get_value()


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueueCharacter(self, val):
        buffer_node = Node(val)
        if self.head == None:
            self.head = buffer_node
            self.tail = buffer_node
        else:
            self.tail.set_next_node(buffer_node)
            self.tail = buffer_node

    def dequeueCharacter(self):
        if self.head:
            buffer_node = self.head
            self.head = self.head.get_next_node()
            return buffer_node.get_value()


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):

    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
