class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int count = 0;
        int[] res = new int[k];
        List<Integer>[] bucket = new ArrayList[nums.length+1];
        for (int i = 0; i < bucket.length; i++) {
            bucket[i] = new ArrayList<>();
        }
        Map<Integer, Integer> freq = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
        }
        for (int key : freq.keySet()) {
            bucket[freq.get(key)].add(key);
        }
        for (int i = bucket.length-1; i >= 0; i--) {
            if (!bucket[i].isEmpty()) {
                for (int e : bucket[i]) {
                    res[count] = e;
                    count++;
                }
                if (count == k) {
                    break;
                }
            }
        }
        return res;
    }
}

// 4 5 5 6 6 6
// num -> count
// 4 -> 1
// 5 -> 2
// 6 -> 3
// k = 2
// [5, 6]

// frequency map of all elements
// use a heap of size k
// o(n log k)

// vs bucket sort O(n)
// have a list of all elements at the index frequency
