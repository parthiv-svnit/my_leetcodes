class Solution:
    def solveEquation(self, equation: str) -> str:
        i = equation.index('=')
        y1 = equation[:i]
        y2 = equation[i+1:]
        coff1 = 0
        coff2 = 0
        int1 = 0
        int2 = 0
        print(y1, y2)
        
        j = 0
        if 'x' in y1[0] :
            coff1 += 1
            j += 1 
            
        elif y1[0] == '-' :
            if x in y1[1] :
                coff1 -= 1
                j += 2
            elif x in y1[2] :
                coff1 -= int(y1[1])
                j = 3
            else :
                int1 -= int(y1[1])
                j = 2
        elif 'x' in y1[1] :
            coff1 += int(y1[0])
            j += 2
        else :
            int1 += int(y1[0])
            j += 1

        while j < (i) :
            if y1[j] == '+' :
                print(y1[j + 1])
                if j + 1 < i and 'x' in y1[j + 1] :
                    coff1 += 1
                    j += 2

                elif j + 2 < i and 'x' in y1[j + 2] :
                    coff1 += int(y1[j + 1])
                    j += 3

                else :
                    int1 += int(y1[j + 1])
                    j += 2

            elif y1[j] == '-' :
                print(y1[j + 1])
                if j + 1 < i and 'x' in y1[j + 1] :
                    coff1 -= 1
                    j += 2

                elif j + 2 < i and 'x' in y1[j + 2] :
                    coff1 -= int(y1[j + 1])
                    j += 3
                    
                else :
                    int1 -= int(y1[j + 1])
                    j += 2

            else :
                coff1 += int(y1[j])
                j += 1
        j = 0
        ly2 = len(y2)
        
        if 'x' in y2[0] :
            coff2 += 1
            j += 1 
            
        elif y2[0] == '-' :
            if x in y2[1] :
                coff2 -= 1
                j += 2
            elif x in y2[2] :
                coff2 -= int(y2[1])
                j = 3
            else :
                int2 -= int(y2[1])
                j = 2
        elif 'x' in y2[1] :
            coff2 += int(y2[0])
            j += 2
        else :
            int2 += int(y2[0])
            j += 1

        while j < (ly2) :
            if y2[j] == '+' :
                print(y2[j + 1])
                if j + 1 < ly2 and 'x' in y2[j + 1] :
                    coff2 += 1
                    j += 2

                elif j + 2 < ly2 and 'x' in y2[j + 2] :
                    coff2 += int(y2[j + 1])
                    j += 3

                else :
                    int2 += int(y2[j + 1])
                    j += 2

            elif y2[j] == '-' :
                print(y2[j + 1])
                if j + 1 < ly2 and 'x' in y2[j + 1] :
                    coff2 -= 1
                    j += 2

                elif j + 2 < ly2 and 'x' in y2[j + 2] :
                    coff2 -= int(y2[j + 1])
                    j += 3
                    
                else :
                    int2 -= int(y2[j + 1])
                    j += 2

            else :
                coff2 += int(y2[j])
                j += 1

        print(int1, coff1)
        print(int2, coff2)