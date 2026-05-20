class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        print(f"corresponding {corresponding}")

        for val in s: 
            if val in corresponding.values():
                stack.append(val)
            else:
                if stack:
                    if stack[-1] == corresponding[val]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0: 
            return True 
        else:
            return False
"""
1. Look through each string 
2. if x is the opening string 
    3. append it to the stack 
4. if its not then 
    5. check if theres anything in the stack
        6. if yes 
            7. pop the first element 
        8. if no 
            9. then return False
10. check len, if len = 0 then return true, false otherwise
"""












