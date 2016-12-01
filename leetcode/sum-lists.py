"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    @staticmethod
    def addTwoNumbers(list1, list2):
        lengthOfList1 = Solution().lengthOfList(list1)
        lengthOfList2 = Solution().lengthOfList(list2)

        if lengthOfList1 > lengthOfList2:
            list2 = Solution().makeSameLength(list2, lengthOfList1 - lengthOfList2)
        elif lengthOfList1 < lengthOfList2:
            list1 = Solution().makeSameLength(list1, lengthOfList2 - lengthOfList1)


        return Solution().calculateSum(list1, list2)

    @staticmethod
    def lengthOfList(list):
        len = 0
        while list:
            len = len+1
            list = list.next

        return len

    @staticmethod
    def calculateSum(l1, l2):
        carry = 0
        sum = 0
        final_list = None
        start_of_final_list = None

        while l1:
            sum = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) / 10

            node = ListNode(sum)
            if start_of_final_list is None:
                final_list = node
                start_of_final_list = node
            else:
                final_list.next = node
                final_list = final_list.next

            l1 = l1.next
            l2 = l2.next


        if carry > 0: final_list.next = ListNode(carry)

        return start_of_final_list

    @staticmethod
    def makeSameLength(list, count):
        listStart = list

        while list.next:
            list = list.next

        for times in range(count):
            list.next = ListNode(0)
            list = list.next

        return listStart


# Test
# if __name__ == "__main__":
#     node = ListNode(1)
#     node.next = ListNode(1)
#     node.next.next = ListNode(7)
#     node.next.next.next = ListNode(4)
#
#     nn = ListNode(9)
#     nn.next = ListNode(9)
#
#     Solution().addTwoNumbers(node, nn)
