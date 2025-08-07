def longestValidParentheses(s: str) -> int:
    stack = []
    n = len(s)
    res = []
    stash = 0
    for i in range(n):
        targ = s[i]
        if targ == "(":
            stack.append(targ)
            res.append(0)
        else:
            if len(stack) > 0:
                stack.pop()
                stash = res.pop()
                # print(f"{stash=}")
                if res == []:
                    res.append(2 + stash)
                else:
                    res[-1] += 2 + stash
            else:
                res.append(0)
        # print(f"{stack=}")
        # print(f"{res=}")
    return max(res) if len(res) > 0 else 0


print(longestValidParentheses("(()"))  # Expected: 2
print(longestValidParentheses(")()())"))  # Expected: 4
