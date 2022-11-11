class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=-1,j=0;
        while(j<nums.size()){
            if(j+1<nums.size() && nums[j]==nums[j+1]){
                j++;
                continue;
            }
            swap(nums[i+1],nums[j]);
            i++;j++;
        }
    return i+1;

    }
};