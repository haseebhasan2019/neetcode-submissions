class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();
        for (String str : strs) {
            boolean added = false;
            for (String key : anagrams.keySet()) {
                if (isAnagram(str, key)) {
                    anagrams.get(key).add(str);
                    added = true;
                    break;
                }
            }
            if (!added) {
                anagrams.put(str, new ArrayList<String>(Arrays.asList(str)));
            }
        }
        List<List<String>> res = new ArrayList<>();
        for (String key : anagrams.keySet()) {
            res.add(anagrams.get(key));
        }
        return res;
    }
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> mapS = new HashMap<>();
        HashMap<Character, Integer> mapT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            mapS.put(s.charAt(i), 1 + mapS.getOrDefault(s.charAt(i), 0));
            mapT.put(t.charAt(i), 1 + mapT.getOrDefault(t.charAt(i), 0));
        }
        return mapS.equals(mapT);
    }

}
