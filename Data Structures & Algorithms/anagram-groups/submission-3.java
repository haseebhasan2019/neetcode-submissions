class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();
        for (String str : strs) {
            int[] count = new int[26];
            for (char c : str.toCharArray()) {
                count[c-'a']++;
            }
            anagrams.putIfAbsent(Arrays.toString(count), new ArrayList<String>());
            anagrams.get(Arrays.toString(count)).add(str);
        }
        return new ArrayList<>(anagrams.values());
    }
}
