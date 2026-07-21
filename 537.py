class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        arr1 = num1.split('+')
        arr2 = num2.split('+')
        arr1[0] = int(arr1[0])
        arr2[0] = int(arr2[0])
        arr1[1] = int(arr1[1][:-1])
        arr2[1] = int(arr2[1][:-1])
        print(arr1, arr2)
        arr = []

        arr.append((arr1[0] * arr2[0]) - (arr1[1] * arr2[1]))
        arr.append((arr1[0] * arr2[1]) + (arr1[1] * arr2[0]))
        print(arr)

        return str(arr[0]) + "+" + str(arr[1]) + "i"