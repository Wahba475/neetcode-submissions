
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     output={}

     for i in range(len(nums)):
      complement=target-nums[i]
      if complement in output:
         return [output[complement],i]
      else:
        output[nums[i]]=i



        