class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();
        for (String str : strs) {
            int[] word = new int[26];
            for (char c : str.toCharArray()) word[c-'a']++;
            if (anagrams.containsKey(Arrays.toString(word))) {
                anagrams.get(Arrays.toString(word)).add(str);
            } else {
                anagrams.put(Arrays.toString(word), new ArrayList<>(List.of(str)));
            }
        }
        return new ArrayList<>(anagrams.values());
    }
}
