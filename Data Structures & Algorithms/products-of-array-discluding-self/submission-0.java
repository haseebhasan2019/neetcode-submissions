class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] leftProduct = new int[nums.length];
        int[] rightProduct = new int[nums.length];

        leftProduct[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            leftProduct[i] = leftProduct[i-1] * nums[i];
        }

        rightProduct[nums.length-1] = nums[nums.length-1];
        for (int i = nums.length-2; i >= 0; i--) {
            rightProduct[i] = rightProduct[i+1] * nums[i];
        }

        nums[0] = rightProduct[1];
        nums[nums.length-1] = leftProduct[nums.length-2];
        for (int i = 1; i < nums.length-1; i++) {
            nums[i] = leftProduct[i-1] * rightProduct[i+1];
        }
        System.out.println(Arrays.toString(leftProduct));
        System.out.println(Arrays.toString(rightProduct));

        return nums;

    }
}  
/*
[1  2  4  6]
[1  2  8  48] ->
[48 48 24 6] <-

[48 24 12 8]


[-1 0 1 2 3]
[-1 0 0 0 0] ->
[ 0 0 6 6 3] <-

[0 -6 0 0 0]


*/