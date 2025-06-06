def strStr(haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        res = -1
        print(f"{m=}   {n=}")
        for i in range(n - m + 1):
            print(f"{haystack[i:i + m]=}")
            if haystack[i:i + m] == needle:
                res = i
                break
            else:
                res = -1
        return res
      
# The above code is a simple implementation of the strStr function, which finds the first occurrence of a substring (needle) in a string (haystack).
if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    result = strStr(haystack, needle)
    print(f"Result: {result}")  # Expected output: 2, since "ll" starts at index 2 in "hello".