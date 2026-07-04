class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupeSet = set()
        for num in nums:
            noDupeSet.add(num)

        if len(noDupeSet) < len(nums):
            return True
        return False