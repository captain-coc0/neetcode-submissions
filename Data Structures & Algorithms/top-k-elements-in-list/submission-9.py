from heapq import _heapify_max

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqBucket = {}
        for num in nums:
            freqBucket[num] = freqBucket.get(num, 0) + 1
        freqTuples = [[] for i in range(len(nums)+1)]
        for key, value in freqBucket.items():
            freqTuples[value].append(key)
        maxlist = []
        for i in range(len(freqTuples)-1, 0, -1):
            for num in freqTuples[i]:
                maxlist.append(num)
                if len(maxlist) == k:
                    return maxlist
        return maxList

