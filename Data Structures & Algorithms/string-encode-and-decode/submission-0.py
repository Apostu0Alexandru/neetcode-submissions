class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        p1 = 0
        res = []
        while (p1<len(s)):
            p2 = p1
            while(s[p2]!="#"):
                p2+=1
            length = int(s[p1:p2])
            payload = s[p2+1:p2+1+length]
            res.append(payload)
            p1 = p2 + 1 + length
        return res