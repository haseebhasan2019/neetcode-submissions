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
            String num = "";
            while (str.charAt(i) != '#') {
                num += str.charAt(i);
                i++;
            }
            i++;
            int length = Integer.parseInt(num);
            String word = str.substring(i,i+length);
            res.add(word);
            i+=length;
        }
        return res;
    }
}
