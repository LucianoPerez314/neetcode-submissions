class Solution:
    def jump(self, nums: List[int]) -> int:
        # # minimum nmber of jumps from start = 1 + min(minimum number of jumps from next possible jump destinations)
        # memo = {}
        # def dp(i):
        #     # memo
        #     if i in memo:
        #         return memo[i]

        #     # base cases
        #     if i >= len(nums) - 1:
        #         memo[i] = 0
        #         return memo[i]

        #     # recursive cases
        #     max_jump_len = nums[i]
        #     memo[i] = len(nums)
        #     for j in range(i+1, i + max_jump_len + 1):
        #         memo[i] = min(memo[i], 1 + dp(j))

        #     return memo[i]
        # return dp(0) 

        # When you iterate through the array and hit current_end, you are forced to take another jump, updating current_end to farthest.
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Stop at len(nums) - 1 because once you reach or pass the last index, no more jumps are needed
        for i in range(len(nums) - 1):
            # Track the farthest index reachable from the current jump window
            farthest = max(farthest, i + nums[i])
            
            # Reached the end of the current jump's range; commit to the next jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Optional early exit if we can already reach the end
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps