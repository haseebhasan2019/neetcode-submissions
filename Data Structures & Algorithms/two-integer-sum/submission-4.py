from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if target % 2 == 0:
            i = None
            for index, num in enumerate(nums):
                if (num == target/2):
                    if i == None:
                        i = index
                    else:
                        return [i,index]
        d = {num: i for i, num in enumerate(nums)}
        for num, i in d.items():
            if (target - num) in d and d.get(target-num) != i:
                return [i, d.get(target-num)]