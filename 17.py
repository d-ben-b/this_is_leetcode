from typing import List
def letterCombinations(digits: str) -> List[str]:
    dic = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }
    first = []
    temp = []

    for digit in digits:
        print(f'The digit is {digit}')
        if first == []:
            first = dic[digit]
        else:
            temp = []
            for element in first:
                for char in dic[digit]:
                    print(f'{digit=}   {element=}   {char=}')
                    temp.append(element+char)
            first = temp #^ call by reference
            print(f"{first=}")
    return first

# Test the function
if __name__ == "__main__":
    digits = "234"
    result = letterCombinations(digits)
    print(result)