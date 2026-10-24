class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        index = 0
        sorted_nums = sorted(nums)
        while index < len(sorted_nums) - 2:
            if index > 0 and sorted_nums[index] == sorted_nums[index - 1]:
                index += 1
                continue
            lindex = index + 1
            rindex = len(sorted_nums) - 1
            target = -sorted_nums[index]
            while lindex < rindex:
                summa = sorted_nums[lindex] + sorted_nums[rindex]
                if summa == target:
                    pair = [sorted_nums[index], sorted_nums[lindex], sorted_nums[rindex]]
                    l.append(pair)
                    lindex += 1
                    rindex -= 1
                    while lindex < rindex and sorted_nums[lindex] == sorted_nums[lindex - 1]:
                        lindex += 1
                    while lindex < rindex and sorted_nums[rindex] == sorted_nums[rindex + 1]:
                        rindex -= 1
                elif summa > target:
                    rindex -= 1
                else:
                    lindex += 1
            index += 1
        return l