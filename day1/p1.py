from functools import reduce
from typing import List, Tuple


GOAL_NUM = 2020


def get_input(filename: str) -> List[int]:
  """Returns contents of filename as list of ints"""
  with open(filename,'r') as fh:
    lines = fh.readlines()

  return [int(x.strip()) for x in lines]


def find_2_nums_2020(
    numbers: List[int]
  ) -> Tuple[int, int]:
  """Returns first tuple from numbers that sums to 2020"""
  for i, num1 in enumerate(numbers):
    for num2 in numbers[i:]:
        if num1 + num2 == 2020:
            return (num1, num2)


def find_3_nums_2020(
    numbers: List[int]
  ) -> Tuple[int, int]:
  """Returns first tuple from numbers that sums to 2020"""
  for i, num1 in enumerate(numbers):
    for j, num2 in enumerate(numbers[i+1:]):
        for num3 in numbers[j+1:]:
            if num1 + num2 + num3 == 2020:
                return (num1, num2, num3)

def find_nums_2020(
    nums: List[int], count: int = 2, index: int = 0, partial_nums: List[int] = []
) -> List[int]:
    """"""
    if count == 0:
        if reduce(lambda x,y: x+y, partial_nums) == GOAL_NUM:
            return partial_nums
        return

    for i in range(index, len(nums)):
        new_partial = partial_nums+[nums[i]]
        result = find_nums_2020(nums, count-1, index+i, new_partial)
        if result: 
            return result        

    # breakpoint()
    # if reduce(lambda x,y: x+y, partial_nums) > GOAL_NUM:
    #     return

    # if count > 1:
    #     for i in range(index,len(nums)): 
    #         updated = partial_nums+[nums[i]]
    #         result = find_nums_2020_recurse(nums, count-1, index+i, updated)
    #         if result: 
    #             return result

    # for num in nums[index:]:
    #     temp_list = partial_nums+[num]
    #     if reduce(lambda x,y: x+y, temp_list) == 6:
    #         return temp_list

# def find_nums_2020(nums: List[int], count: int = 2) -> List[int]:
#     return find_nums_2020_recurse(nums, count-1, 1, [nums[0]])

def product(nums: List[int]) -> int:
    """Returns product of nums"""
    return reduce(lambda x,y: x*y, nums, 1)


def product_from_2020(filename) -> int:
  """Returns produce of first 2 nums in filename that sum to 2020"""
  numbers = get_input(filename)
  nums2 = find_2_nums_2020(numbers)
  # nums2_v2 = find_nums_2020(numbers, 2)
  # print(nums2, nums2_v2)

  nums3 = find_3_nums_2020(numbers)
  nums3_v2 = find_nums_2020(numbers, 3)
  print(nums3, nums3_v2)

  return product(nums2), product(nums3)


output = product_from_2020("./input.txt")
print(output)

