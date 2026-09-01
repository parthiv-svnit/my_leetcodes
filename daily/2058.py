# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        
        arr = []
        count = 1
        while temp.next.next :
            if temp.val < temp.next.val and temp.next.val > temp.next.next.val :
                arr.append(count)
            elif temp.val > temp.next.val and temp.next.val < temp.next.next.val :
                arr.append(count)
            count += 1
            temp = temp.next
        print(arr)
        if not arr or len(arr) == 1 :
            return [-1, -1]
        # arr.sort()
        minv = float('inf')
        for i in range(len(arr) - 1) :
            minv = min(minv, arr[i + 1] - arr[i])
        return [minv, arr[-1] - arr[0]]