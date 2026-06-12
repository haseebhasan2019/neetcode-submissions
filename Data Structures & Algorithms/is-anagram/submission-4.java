class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> mapS = new HashMap<>();
        HashMap<Character, Integer> mapT = new HashMap<>();
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            mapS.put(s.charAt(i), 1 + mapS.getOrDefault(s.charAt(i), 0));
            mapT.put(t.charAt(i), 1 + mapT.getOrDefault(t.charAt(i), 0));
        }
        return mapS.equals(mapT);
    }
}
