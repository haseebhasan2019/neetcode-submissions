class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> sMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            sMap.put(c, sMap.getOrDefault(c,0)+1);
        }
        for (char c : t.toCharArray()) {
            Integer res = sMap.get(c);
            if (res == null) {
                return false;
            }
            if (res == 1) {
                sMap.remove(c);
            } else {
                sMap.put(c, res-1);
            }
        }
        return sMap.size() == 0;


    }
}
