class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair (temp, index)
        # Iterate through temps
        for i, t in enumerate(temperatures):
            # Compare current temp to every previous temp whose index
            # hasn't been filled yet.
            # And if the current temp is greater than the previous temps,
            while stack and t > stack[-1][0]:
                # remove the previous temp from the history.
                stackT, stackI = stack.pop()
                # populate result via the differences in index.
                res[stackI] = (i - stackI) 
            # append current temp to history for later evaluation.
            stack.append([t, i])

        return res



           

        