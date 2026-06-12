from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # if key doesn't exist will create
        for word in strs:
            sortedWord = "".join(sorted(word))
            anagrams[sortedWord].append(word)
        return list(anagrams.values())