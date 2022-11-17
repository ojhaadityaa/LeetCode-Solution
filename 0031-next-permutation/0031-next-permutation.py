class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Breakflag = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                index = i-1
                Breakflag = 1
                for j in range(len(nums)-1,index,-1):
                    if nums[j] > nums[index]:
                        nums[j], nums[index] =  nums[index], nums[j]
                        nums[index+1:] = nums[index+1:][::-1]
                        break
                break
        if not Breakflag: nums.reverse()
        