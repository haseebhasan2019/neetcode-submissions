class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for letter in word:
                letters[ord(letter)-ord('a')]+=1
            anagram_map[tuple(letters)].append(word)
        return list(anagram_map.values())

# 1. Hashmap of a word to its list of anagrams
# - call isAnagram against each key for each word O(k) * keys (worst case n) * n (words)
# 2. key is sorted word
# - append directly to the sorted word's list O(klogk) * n (words)
# 3. key is a tuple representation of an array representation of the letter frequency
# - O(k) * n where k is the length of the longest word