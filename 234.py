# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        arr = []
        temp = head
        while temp :
            arr.append(temp.val)
            temp = temp.next
        n = len(arr)
        for i in range(n // 2) :
            if arr[i] != arr[n - i - 1] :
                return False
        return True