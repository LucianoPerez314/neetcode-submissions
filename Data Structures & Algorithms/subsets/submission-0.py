class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Create all possible bit permutations to determine when to include and exclude numbers in nums.
        l = len(nums)
        flags = [format(i, f"0{l}b") for i in range(1 << l)]
        print(flags)
        res = []
        for bitstring in flags:
            arr = []
            for i, bit in enumerate(bitstring):
                if int(bit) == 1:
                    arr.append(nums[i])
            res.append(arr)
        return res