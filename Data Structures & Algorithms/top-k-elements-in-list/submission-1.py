class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashSeen={}
        output=[]

        for i in range(len(nums)):
            hashSeen[nums[i]]=hashSeen.get(nums[i],0)+1

        while(k!=0 and len(hashSeen)!=0):
            biggest=max(hashSeen,key=hashSeen.get)
            output.append(biggest)
            del hashSeen[biggest]
            k=k-1 

        return output       


        