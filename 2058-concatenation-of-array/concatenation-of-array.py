class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        box = []
        box += nums
        box += nums
        return box