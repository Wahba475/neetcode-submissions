class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        output=[]


        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1


        while k>0:
            max_key=max(seen,key=seen.get)
            output.append(max_key)
            del seen[max_key]
            k-=1
        return output    
            





        