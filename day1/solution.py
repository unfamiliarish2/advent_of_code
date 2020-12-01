from functools import reduce
from typing import List, Tuple


GOAL_NUM = 2020


def get_input(filename: str) -> List[int]:
    """Returns contents of filename as list of ints"""
    with open(filename,'r') as fh:
        lines = fh.readlines()

    return [int(x.strip()) for x in lines]


def sum(nums: List[int]) -> int:
    """Returns sum of nums"""
    return reduce(lambda x,y: x+y, nums, 1)    


def product(nums: List[int]) -> int:
    """Returns product of nums"""
    return reduce(lambda x,y: x*y, nums, 1)


def find_nums_2020(
    input_nums: List[int], count: int = 2, summands: List[int] = []
) -> List[int]:
    """Finds and returns `count` numbers from `input_nums` that sum to GOAL_NUM"""
    # partial sum too high, break current loop
    if summands and sum(summands) > GOAL_NUM:
        return

    # base case, check sum
    if count == 0:
        if sum(summands) == GOAL_NUM:
            return summands
        return

    # recursive step
    for i, num in enumerate(input_nums):
        result = find_nums_2020(input_nums[i+1:], count-1, summands+[num])
        if result: 
            return result     


def products_from_2020(filename: str) -> int:
    """Returns products of first 2 nums and 3 nums in filename that sum to 2020"""
    numbers = get_input(filename)
    factors2 = find_nums_2020(numbers, 2)
    factors3 = find_nums_2020(numbers, 3)

    return product(factors2), product(factors3)


products = products_from_2020("./input.txt")
print(f"2 numbers product: {products[0]}")
print(f"3 numbers product: {products[1]}")
