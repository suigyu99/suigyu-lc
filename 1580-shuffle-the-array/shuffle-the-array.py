class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        HalfNum = len(nums) // 2
        box = []
        for i in range(HalfNum):
            box.append(nums[i])
            box.append(nums[i + HalfNum])
        return box