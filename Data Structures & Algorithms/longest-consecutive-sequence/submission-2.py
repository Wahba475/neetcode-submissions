class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest=0

        nums1=sorted(nums)
        current=1
        if(len(nums)==0):
            return 0
        
        for i in range(len(nums1)-1):
         
            if(nums1[i+1]==nums1[i]+1):
                current+=1
            elif(nums1[i+1]==nums1[i]):
                pass
            else:
                longest=max(longest,current)
                current=1  
        longest=max(longest,current)        
             
        return longest        



      