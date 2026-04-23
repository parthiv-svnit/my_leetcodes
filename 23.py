# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        listo = ListNode(0)
        temp = listo
        k = len(lists)
        while True :
            minv = float('inf')
            mini = -1

            for j in range(k) :
                if lists[j] :
                    if lists[j].val < minv :
                        minv = lists[j].val
                        mini = j

            if mini == -1:
                break

            temp.next = lists[mini]
            temp = temp.next
            lists[mini] = lists[mini].next

        return listo.next