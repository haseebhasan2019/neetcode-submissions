class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) freq.merge(num, 1, Integer::sum);

        List<Integer>[] bucket = new ArrayList[nums.length+1];
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            if (bucket[e.getValue()] == null) bucket[e.getValue()] = new ArrayList<>();
            bucket[e.getValue()].add(e.getKey());
        }
        int count = 0;
        int[] res = new int[k];

        for (int i = bucket.length-1; i >= 0; i--) {
            if (bucket[i] != null) {
                for (int e : bucket[i]) {
                    res[count++] = e;
                }
                if (count == k) break;
            }
        }
        return res;
    }
}