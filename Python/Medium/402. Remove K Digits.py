class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num)==k:
            return "0"
        
        number_remove=k
        stack = []
            
        for current in num:
            while number_remove and stack and int(stack[-1])>int(current):
                stack.pop()
                number_remove-=1
            stack.append(current)
                
        if number_remove:
            stack = stack[:len(stack)-number_remove]
            
        stack = "".join(stack).lstrip("0")
        
        if stack:
            return stack
        else:
            return "0"