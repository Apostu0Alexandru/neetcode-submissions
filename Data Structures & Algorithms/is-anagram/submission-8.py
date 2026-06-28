class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s)!=len(t)):
            return False

        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                return False
        
        if all(count == 0 for count in freq.values()):
            return True
        else:
            return False