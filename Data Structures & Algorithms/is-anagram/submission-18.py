class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

'''
Input: s = "racecar", t = "carrace"
s = {
    a: 2
    c: 2
    r: 2
    e: 1
}
t = {
    a: 2
    c: 2
    r: 2
    e: 1
}

1 5 7 9,  t = 12




'''