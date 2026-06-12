class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n = number of words
        # m = length of the longest word
        # Sorting every word would be O(n * mlogm) time
        # Create a array fingerprint for each word and use that instead of sorting
        # O(n * m) time
        # O(n * m) + O(n) * 26  = O(n * m) space
        anagrams = defaultdict(list)
        for word in strs:
            word_arr = [0] * 26
            for c in word:
                word_arr[ord(c) - ord('a')] += 1
            anagrams[tuple(word_arr)].append(word)
        return list(anagrams.values())
