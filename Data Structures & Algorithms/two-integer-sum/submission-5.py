class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,n in enumerate(nums):
            if target - n in hash and i != hash[target - n]:
                return [hash[target - n],i,]
            hash[n]=i

        