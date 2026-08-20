class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        f = {}

        for x in nums:
            if x in f:
                f[x] = f[x] + 1
            else:
                f[x] = 1


        
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in f.items():
            buckets[count].append(number)

        res = []

        for x in range(len(buckets)-1, 0, -1):
            for num in buckets[x]:
                res.append(num)
                if len(res) == k:
                    return res
