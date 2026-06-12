class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, 1+counts.getOrDefault(num, 0));
        }
        PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.getValue(), b.getValue()));
        for (Map.Entry<Integer, Integer> e : counts.entrySet()) {
            if (heap.size() < k) {
                heap.offer(e);
            } else {
                if (e.getValue() > heap.peek().getValue()) {
                    heap.poll();
                    heap.offer(e);
                }
            }
        }
        int[] res = new int[k];
        for (int i = 0; i < k; i++){
            res[i] = heap.poll().getKey();
        }
        return res;
    }
}
