class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = str(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())

# 1. Hashmap of a word to its list of anagrams
# - call isAnagram against each key for each word O(k) * keys (worst case n) * n (words)
# 2. key is sorted word
# - append directly to the sorted word's list O(klogk) * n (words)