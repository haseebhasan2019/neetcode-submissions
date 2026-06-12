class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            word_arr = [0] * 26
            for c in word:
                word_arr[ord(c) - ord('a')] += 1
            anagrams[tuple(word_arr)].append(word)
        return list(anagrams.values())
