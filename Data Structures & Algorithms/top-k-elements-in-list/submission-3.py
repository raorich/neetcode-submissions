class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cout = Counter()
        res=[]
        freq=Counter(nums)
        print(freq.most_common())

        for elem,freq in freq.most_common(k):
            res.append(elem)
        return res