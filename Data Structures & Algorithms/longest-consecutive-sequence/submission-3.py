class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       seen = set(nums)
       longest = 0
       for x in nums:
            if x - 1 not in seen:
                streak = 1
                p = 1
                while x + p in seen:
                    streak += 1
                    p += 1
                longest = max(longest, streak)
       return longest