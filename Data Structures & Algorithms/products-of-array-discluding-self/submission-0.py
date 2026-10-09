class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 1
        output = []
        for num in nums:
            output.append(i)
        
        product = 1
        prefix = 1
        sufix = 1
        index = 0
        while(index<len(nums)): 
            output[index] = prefix
            prefix = prefix * nums[index]
            index += 1
        while(index>0):
            output[index-1] = output[index -1 ] * sufix
            sufix = sufix * nums[index -1]
            index -=1 
        return output