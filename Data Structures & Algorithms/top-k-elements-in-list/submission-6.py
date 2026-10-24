class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq=Counter(nums)
        print(freq.most_common(2))

        for elem,freq in freq.most_common(k):
            res.append(elem)
        return res
    
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for e in freq[i]:
                res.append(e)
                if len(res) == k:
                    return res