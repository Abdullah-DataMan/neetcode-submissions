class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1

        for i in range(k):
            Max_key = max(hashMap, key=hashMap.get)
            hashMap[Max_key] = 0
            result.append(Max_key)

        return result

        