class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        bucket=[]
        output=[]

        for i in range(len(nums)+1):
            bucket.append([])


        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1


        for key,value in seen.items():
            bucket[value].append(key)


        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                output.append(num)
            if(len(output)==k):
                return output    

       







        