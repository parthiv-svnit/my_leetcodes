class Solution:
    def solveEquation(self, equation: str) -> str:
        
        y1, y2 = equation.split("=")

        def evaluate(s):
            coeff = 0
            const = 0
            
            i = 0
            n = len(s)

            while i < n:
                sign = 1

                if s[i] == '+':
                    i += 1
                elif s[i] == '-':
                    sign = -1
                    i += 1

                num = 0
                has_num = False

                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                    has_num = True

                if i < n and s[i] == 'x':
                    if not has_num:
                        num = 1
                    coeff += sign * num
                    i += 1
                else:
                    const += sign * num

            return coeff, const

        lc, lv = evaluate(y1)
        rc, rv = evaluate(y2)

        coeff = lc - rc
        const = rv - lv

        if coeff == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        return "x=" + str(const // coeff)