class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            anagrams[tuple(freq)].append(word)
        return [v for k, v in anagrams.items()]

'''
how to tell if two words are anagrams:
1. convert the words into frequency maps and compare the maps - O(n) time, O(n) extra space
2. sort the words and compare - O(nlogn) time, O(1) extra space

to group together anagrams = map a word to all of its anagrams
1. for m words, worst case no anagrams, go through all keys in the map to see if it an anagram - O(m^2*n) time, O(n) extra space where n is the longest word
2. for m words, sort the word, see if it exists in the map, if it does, add original word to its anagram list, else add it - O(m * nlogn) time, O(m*n) extra space for each sorted word
3. Instead of storing the sorted word as the key, store a freq representation of it O(m*n) time O(m) extra space
'''