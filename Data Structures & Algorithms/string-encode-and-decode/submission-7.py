class Solution:

    def encode(self, strs: List[str]) -> str:
        for i, s in enumerate(strs):
            strs[i] = str(len(s)) + "#" + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i=j+1
            j=i+length
            string = s[i:j]
            res.append(string)
            i=j
        return res
