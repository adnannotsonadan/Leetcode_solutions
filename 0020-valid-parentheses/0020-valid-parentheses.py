class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack = []  

        # for ch in s:
        #     if ch in "({[":
        #         stack.append(ch)  
        #     else:
        #         if not stack:
        #             return False  
        #         top = stack.pop()

                
        #         if (ch == ')' and top == '(') or (ch == ']' and top == '[') or (ch == '}' and top == '{'):
        #             continue
        #         else:
        #             return False

        # return len(stack) == 0
        stack=[]
        for x in s:
            if x in "([{":
                stack.append(x)
            else:
                if not stack:
                    return False
                    
                if x==')' and stack[-1]=='(' or x==']' and stack[-1]=='[' or x=='}' and stack[-1]=='{':
                    stack.pop()  
                else:
                    return False
                    
        if len(stack)==0:
            return True
        
        else:
            return False
            
            