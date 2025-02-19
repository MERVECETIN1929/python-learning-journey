class MyHashSet(object):

    def __init__(self):
        self.set = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set.add(key)

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
