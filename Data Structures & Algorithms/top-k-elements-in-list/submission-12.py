import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqBucket = {}
        for num in nums:
            freqBucket[num] = freqBucket.get(num, 0) + 1

        freqTuples = []
        for key, value in freqBucket.items():
            freqTuples.append((value,key))

        res = []
        heapq.heapify_max(freqTuples)
        for i in range(k):
            res.append(heapq.heappop_max(freqTuples)[1])

        return res

