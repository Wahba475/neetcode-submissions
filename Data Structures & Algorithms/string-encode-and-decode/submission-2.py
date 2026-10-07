class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded=""

        for c in strs:
            n=len(c)
            encoded+=str(n)+"#"+c

        return encoded

    def decode(self,encoded:str)-> List[str]:

      
        sol=[]
        i=0
        while i<len(encoded):
            size=""
            while encoded[i]!='#':
                size+=encoded[i]
                i+=1
            i+=1
            size=int(size)  
            output=""
            while size>0:
                output+=encoded[i]
                i+=1
                size-=1
            sol.append(output)    
        return sol          

            

        