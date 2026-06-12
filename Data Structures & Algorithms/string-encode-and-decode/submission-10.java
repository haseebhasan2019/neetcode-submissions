class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append(str.length() + "#" + str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int hashIdx = str.indexOf('#', i);
            int length = Integer.parseInt(str.substring(i, hashIdx));
            i = hashIdx + 1;
            res.add(str.substring(i,i+length));
            i+=length;
        }
        return res;
    }
}
