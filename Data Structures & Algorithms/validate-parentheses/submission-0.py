class Solution:
    def isValid(self, s: str) -> bool:
        types={")":"(", "}":"{" , "]":"["}
        stack=[]
        for elem in s:
            if elem in types:
                if stack and stack[-1] == types[elem]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(elem)
        
        return stack == []