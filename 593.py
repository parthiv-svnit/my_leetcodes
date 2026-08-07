class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4 :
            return False
        def dis(p1, p2) :
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        arr = []
        arr.append(dis(p1, p2))
        arr.append(dis(p1, p3))
        arr.append(dis(p1, p4))
        arr.append(dis(p2, p3))
        arr.append(dis(p2, p4))
        arr.append(dis(p3, p4))

        arr.sort()
        if arr[0] != arr[1] :
            return False
        if arr[0] != arr[2] :
            return False
        if arr[0] != arr[3] :
            return False
        if arr[4] != arr[5] :
            return False
        if arr[4] != 2 * arr[0] :
            return False
        return True