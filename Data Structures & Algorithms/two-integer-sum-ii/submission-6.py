class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left+1, right+1]
            elif two_sum > target:
                right-=1
            else: # two_sum < target:
                left+=1
        return []


# 1 2 3 4 5 6 7 8 9 -> 10

# [1,2,3,4], target = 3