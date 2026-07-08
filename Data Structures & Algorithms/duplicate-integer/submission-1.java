class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        Set<Integer> numbers = new HashSet();
        for(int num: nums){
            if(!(numbers.contains(num))) {
                numbers.add(num);
            }else {
                return true;
            }
        }
        return false;
        
    }
}