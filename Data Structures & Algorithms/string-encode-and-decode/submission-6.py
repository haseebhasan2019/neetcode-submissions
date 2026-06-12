class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello","World"] -> "5#Hello5#World"
        # ["123","4567"] -> "3#1234#4567"
        # ["##", "22", "##"] -> "2###2#222###"
        for i, s in enumerate(strs):
            strs[i] = str(len(s)) + "#" + strs[i]
        res = "".join(strs)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length_str = ""
            while s[i] != '#':
                length_str+=s[i]
                i+=1
            length = int(length_str)
            i+=1
            string = ""
            for index in range(i,i+length):
                string+=s[index]
                i+=1
            res.append(string)
        return res
