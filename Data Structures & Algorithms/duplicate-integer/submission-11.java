class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> check = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            check.add(nums[i]);
        }
        return check.size() != nums.length;
    }
}
