class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            //if the array contains a plus or minus
            int num = nums[i];
            if (!set.contains(num-1)) {
                int len = 1;
                while (set.contains(num+1)) {
                    len++;
                    num++;
                }
                max = Math.max(max, len);
            }
        }
        return max;

    }
}
/* alternating case
1 10 100 2 11 101 3 12 102

can create a list of sets - handle them as clusters
and keep adding to their lengths

iterate through the list of sets to see which one to add to

*/