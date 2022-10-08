class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
            mn=nums[0]+nums[1]+nums[2]
            dif =abs(mn-target)
            n =len(nums)
            print(n)
            nums.sort()
            for i in range(n-2):
                t=nums[i]
                st=i+1
                en =n-1
                print(i)
                while(st<en):
                    sm=nums[st]+nums[en]+nums[i]
                    if sm-target==0:
                        return sm
                    elif sm>target:
                        dif1 =abs(sm-target)
                        if dif1<dif:
                            dif=dif1
                            mn =sm
                        
                        en-=1 
                    else:
                        dif1 =abs(sm-target)
                        if dif1<dif:
                            dif=dif1
                            mn =sm
                        
                        st+=1 
            return mn