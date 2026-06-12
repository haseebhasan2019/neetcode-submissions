from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # if key doesn't exist will create
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] +=1
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())