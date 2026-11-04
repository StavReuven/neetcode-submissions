class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        desc = []
        res = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            while desc and temperatures[desc[-1]] < temp:
                j = desc.pop()
                res[j] = i - j
            desc.append(i)
        

        return res
