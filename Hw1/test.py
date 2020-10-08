def add(num1: int, num2: int = 100) -> str:
    num3 = num1 + num2
    return str(num3)


from typing import List
import math


def listcheck(ans: List[int]):
    print(ans, type(ans))


if __name__ == "__main__":
    # print(add(1))
    # print(add.__annotations__)

    # print(add("456","789"))
    # listcheck([1, 2, 3, 4, 5, 6, 7])
    for i in range(9,-1,-1):
        print(i)