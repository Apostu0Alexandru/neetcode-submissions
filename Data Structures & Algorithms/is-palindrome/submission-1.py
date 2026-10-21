class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        p2 = len(clean_s) - 1
        print(clean_s)
        while(p1<p2):
            if clean_s[p1] != clean_s[p2]:
                 return False
            p1+=1
            p2-=1
        return True