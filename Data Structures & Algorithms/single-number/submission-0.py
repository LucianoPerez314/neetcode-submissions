class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Intuition: XOR is commutative
        # n XOR n = 0
        # thus all duplicates will XOR each other = 0.
        # as for (unique XOR 0...0)
        # --- n XOR 0 = n
        res = 0
        for n in nums:
            res = n ^ res
        return res

        

        