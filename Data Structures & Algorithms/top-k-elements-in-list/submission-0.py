import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        heap = []
        for num, cntr in counter.items():
            heapq.heappush(heap,(cntr, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            count, num = heapq.heappop(heap)
            result.append(num)

        return result