class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        pairs = {'(': ')', '[': ']', '{': '}'}
      
        for char in s :
          if char in pairs:
            stack.append(pairs[char])
          else:
            if(len(stack)==0):
                return False
            elif (stack[-1]!=char) :
                return False 
            else:       
             stack.pop() 

        if(len(stack)==0):
            return True 
        else:
            return False            
       