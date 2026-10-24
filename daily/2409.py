class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        di = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if int(arriveAlice[:2]) > int(leaveBob[:2]) or int(arriveBob[:2]) > int(leaveAlice[:2]) :
            return 0

        if int(arriveAlice[:2]) > int(arriveBob[:2]) :
            a = arriveAlice
        elif int(arriveAlice[:2]) == int(arriveBob[:2]) :
            a = arriveAlice if int(arriveAlice[3:]) > int(arriveBob[3:]) else arriveBob
        else :
            a = arriveBob
        
        if int(leaveAlice[:2]) < int(leaveBob[:2]) :
            b = leaveAlice
        elif int(leaveAlice[:2]) == int(leaveBob[:2]) :
            b = leaveAlice if int(leaveAlice[3:]) < int(leaveBob[3:]) else leaveBob
        else :
            b = leaveBob
        
        # print(a, b)
 
        am = int(a[:2])
        bm = int(b[:2])
        lm = sum(di[am - 1: bm - 1])
        # print(lm)
        ad = int(a[3:])
        bd = int(b[3:])
        ld = bd - ad + 1
        # print(ld)
        return lm + ld if lm + ld >= 0 else 0