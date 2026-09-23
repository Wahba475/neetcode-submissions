class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      group={}

      for i in range(len(strs)):
         text=''.join(sorted(strs[i]))
         if text not in group:
            group[text]=[strs[i]]
         else:
            group[text].append(strs[i])

      return list(group.values())          
