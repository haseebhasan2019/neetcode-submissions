from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map String to list of strings
        d = defaultdict(list)
        for word in strs:
            d[str(sorted(word))].append(word)
        return list(d.values())

# Where n is letters in a word and m is number of words
# sorting m words: O(m * nlogn)
# retrieving m words: m * O(1) = O(m)
# Sorting: O(m * nlogn) + O(m) = O(m * nlogn)

# Call isAnagram on all keys: O(k*n) - depends on the number of keys
    # Worst case: One key per word -> k=m -> O(m) * O(m*n)
# isAnagram: O(m^2*n)