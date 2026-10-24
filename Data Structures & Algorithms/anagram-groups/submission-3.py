class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            size=[0]*26
            for e in s:
                size[ord(e)-ord("a")] +=1
            res[tuple(size)].append(s)
        
        return list(res.values())