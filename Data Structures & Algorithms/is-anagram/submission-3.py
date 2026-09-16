class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


      hashmapS={}
      hashmapT={}

      for i in range(len(s)):
        if s[i] not in hashmapS:
          hashmapS[s[i]]=1
        else:
          hashmapS[s[i]]+=1  

      for i in range(len(t)):
        if t[i] not in hashmapT:
          hashmapT[t[i]]=1
        else:
          hashmapT[t[i]]+=1    

      return hashmapS==hashmapT   


