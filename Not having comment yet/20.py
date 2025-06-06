class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        table = {
            '(':1,
            ')':10,
            '[':2,
            ']':20,
            '{':3,
            '}':30
        }
        for i in range(n):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if table[stack[-1]] * 10 == table[s[i]] :
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0