class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementDict = {}
        for i, v in enumerate(nums):
            if target-v in complementDict:
                return [complementDict[target-v],i]
            complementDict[v] = i
        