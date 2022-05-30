
from typing import List


def twoSum(nums: List[int], target: int):
    d = {}
    for i,j in enumerate(nums) :
        print(i,j);
        n = target - j
        if n in d:
            return [d[n], i]
        else:
             d[j] = i;
 

nums = [2,7,11,15];
target = 9;

value = twoSum(nums, target)
print(value);
