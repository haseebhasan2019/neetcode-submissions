class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For every new anagram, store it in a map [] -> list of words
        anagrams = defaultdict(list) #[] -> list of words
        for word in strs:
            word_arr = [0] * 26
            for c in word:
                word_arr[ord(c) - ord('a')] += 1
            anagrams[tuple(word_arr)].append(word)
        return list(anagrams.values())

# Need to identify anagrams
# Have to have a key for a group of anagrams

# "tha" 

# hat: ["hat"],["tha"]
# act: ["act", "cat"],
# stop: ["stop", "pots", "tops"]