class Solution:
    def minimumPushes(self, word: str) -> int:
        di = Counter(word)
        di = sorted(di.items(), key = lambda x : x[1], reverse = True)
        print(di)
        count = 0
        out = 0
        for i, j in di :
            if count > 23 :
                out += 4 * j
                print(4 * j)
            elif count > 15 :
                out += 3 * j
                print(3 * j)
            elif count > 7 :
                out += 2 * j
                print(2 * j)
            else :
                out += j
                print(j)
            count += 1
        return out