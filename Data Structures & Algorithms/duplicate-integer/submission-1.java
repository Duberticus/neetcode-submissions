//import java.util.Arrays;

class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        boolean result = false;

    for(int i = 0; i <= nums.length-1;i++)
        for(int j = i+1;j <= nums.length-1;j++){
            if(nums[i]== nums[j]){
                result = true;
            }
        }
        return result;
    }
}
