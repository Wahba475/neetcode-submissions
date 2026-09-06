class Solution:
 def productExceptSelf(self, nums: List[int]) -> List[int]:

    left=[]
    right=[]
    prevLeft=1
    prevRight=1
    output=[]
 
    for i in range(len(nums)):
       if(i==0):
          left.append(prevLeft)    
       else:
           prevLeft*=nums[i-1]
           left.append(prevLeft)
        
    for i in range(len(nums)-1,-1,-1):
        if(i==len(nums)-1):
          right.append(prevRight)    
        else:
          prevRight*=nums[i+1]
          right.append(prevRight)

    right.reverse()      

    for i in range(len(nums)):
        output.append(right[i] * left[i])


    return output    


                    
