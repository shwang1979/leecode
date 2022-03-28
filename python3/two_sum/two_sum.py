from typing import List

class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i


if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSum([1, 3, 5, 7], 8)
    print(result)
