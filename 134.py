class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tgas = 0
        tcost = 0
        for i in range(len(gas)) :
            tgas += gas[i]
            tcost += cost[i]
        if tgas < tcost :
            return -1
        
        tank = 0
        i = 0
        j = i
        while j < len(gas) :
            tank += gas[j] - cost[j]
            if tank < 0 :
                tank = 0
                i = j + 1
            j += 1
        return i if i < len(gas) else -1