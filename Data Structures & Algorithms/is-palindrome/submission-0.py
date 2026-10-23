class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=True
        s=s.lower()
        a=""
        for c in s:
            if c.isalnum():
                a+=c
        print(a)

        iter1=len(a)-1
        print(iter1)

        for i in range(int(len(a)/2)):
            if a[i]==a[iter1] and i < iter1:
                iter1-=1
            else:
                return False
        return res
            
