class MyHashSet(object):

    def __init__(self):
        self.set = list()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            self.set.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.set:
            self.set.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.set:
            return True
        else:
            return False


myclass = MyHashSet()
myclass.add("12")
myclass.add("12")
myclass.add("13")
myclass.remove("0")
myclass.remove("12")
print(myclass.contains("0"))
print(myclass.contains("12"))
print(myclass.contains("13"))
print(myclass.set)
