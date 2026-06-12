from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # string -> list[str]
        for word in strs:
            added = False
            for key in anagrams:
                if Counter(word) == Counter(key):
                    anagrams[key].append(word)
                    added = True
            if not added:
                anagrams[word] = [word]
        return [val for val in anagrams.values()]