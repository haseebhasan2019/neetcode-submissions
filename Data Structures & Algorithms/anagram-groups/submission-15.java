class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();
        for (String str : strs) {
            int[] word = new int[26];
            for (char c : str.toCharArray()) word[c-'a']++;
            anagrams.computeIfAbsent(Arrays.toString(word), k -> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(anagrams.values());
    }
}
