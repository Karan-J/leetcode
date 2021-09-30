class Solution {
    public int[] twoSum(int[] nums, int target) {
        int diff = 0;
        // int x[] = x[];
        int y[] = {0,0};
        for (int i = 0; i < nums.length ; i ++) {
            diff = target - nums[i];
            for (int j = 0; j < nums.length ; j++ ) {
                if (diff == nums[j]) {
                    y[0] = i;
                    y[1] = j;
                    break;
                }
            }
        }
        return y;
    }
}

