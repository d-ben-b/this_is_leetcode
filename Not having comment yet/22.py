from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current: str, left: int, right:int):
            if left == 0 and right == 0:
                res.append(current)
            if right > left:
                backtrack(current+")", left, right - 1)
            if left > 0:
                backtrack(current+"(", left - 1, right)
        backtrack("", n, n)
        return  res
#^ 使用回溯法