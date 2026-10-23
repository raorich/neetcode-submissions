class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cout = Counter()
        res=[]
        result=[]
        freq=Counter(nums)
        print(freq.most_common())

        for elem,freq in freq.most_common():
            res.append(elem)
        res=res[0:k]
        return res