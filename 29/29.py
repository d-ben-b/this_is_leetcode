def divide(dividend: int, divisor: int) -> int:
    res = 0
    MAX = 2**31 - 1
    MIN = -1 * 2**31
    answer = 0
    iter = 0
    #! Wrong answer because it require not using multiplication, division, or mod operator.
    # if (dividend ^ divisor) < 0:
    #     answer = math.ceil(dividend / divisor)
    #     res = answer if answer > MIN else MIN
    # else:
    #     answer = dividend // divisor
    #     res = answer if answer < MAX else MAX
    # return res
    while(dividend > divisor and iter < 10):
        print(f"{dividend=}    {divisor=}")
        temp = dividend
        muiltiple = 1
        while(temp > muiltiple * divisor and iter < 10):
            print(f"{temp=}    {muiltiple=}   {divisor=}")
            muiltiple <<= 1
            iter += 1
        res += muiltiple - 1
        temp -= res * divisor
        dividend = temp
        iter += 1
    return res

if __name__ == "__main__":
    dividend = 10
    divisor = 3
    print(divide(dividend, divisor))  # Output: 3
    dividend = 7
    divisor = -3
    print(divide(dividend, divisor))  # Output: 3
    
    