class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        res=0
        if nums:
            res=1
        best=0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                res+=1
                best=max(res,best)
            elif nums[i] == nums[i+1]:
                res=res
            else:
                res=1
        return max(best,res)

        