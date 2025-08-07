# 32. Longest Valid Parentheses

## Problem Statement

Implement the `longestValidParentheses` function that finds the length of the longest valid (well-formed) parentheses substring in a given string containing only '(' and ')'.

### Approach

#### 正面作法

1. **第一次嘗試**:
   - 用`stack`去做題目的紀錄：如果遇到`(`就 push 進去，遇到`)`就 pop 出來，換句話說如果能夠組成一個合理的括號組合：`()()`或是`(())`，`stack`就會是空的，因此可以確保答案至少為 2，先嘗試直接累加 2 的情況，在 test case 中都合理。
   - 問題：在 submit 的時候發現有些 case 不對，像是`()(()`這種情況，需要判斷是否累加或是重置。
2. **第二次嘗試**:

   - 解決方式：把答案變成一串 array:`res[]`，遇到`(`就會 append(0)到 res 中，遇到`)`就會 pop 出來如果並在最後面加 2 或是 append(2)到 res 中

   ```python
   if res == []:
       res.append(2)
   else:
       res[-1] += 2
   ```

- 如果遇到`(()())`的情況會變成
- res = [0] -> [0, 0] -> [2] -> [2, 0] -> [2, 2] ->這一步會把 2 pop 掉所以需要修改一下改成

  ```python
  stash = res.pop()
  if res == []:
    res.append(2 + stash)
  else:
    res[-1] += 2 + stash
  ```
