class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Sum = 0
        Max = 0
        nums.append(0)
        for i in nums:
            if i == 1:
                Sum += 1
            else:
                if Sum > Max:
                    Max = Sum
                Sum = 0
        return Max