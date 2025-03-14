class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list_node = ListNode()
        return_node = new_list_node
        carry = 0
        total_value = 0
        boolean = False
        while l1 or l2:
            if l1 != None:
                total_value += l1.val
                l1 = l1.next
            if l2 != None:
                total_value += l2.val
                l2 = l2.next
            # buradaki kontrol new_list_node değişkeni ilk değerini alacağı zaman için kullanıldı
            if not boolean:
                total_value += carry
                new_list_node.val = (total_value) % 10
                carry = total_value//10
                total_value = 0
                boolean = True
            else:
                total_value += carry
                new_node = ListNode((total_value) % 10)
                carry = total_value//10
                total_value = 0
                new_list_node.next = new_node
                new_list_node = new_list_node.next
        if carry:
            new_node = ListNode(carry)
            new_list_node.next = new_node
        return return_node
