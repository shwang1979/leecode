from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums_len = len(nums)
        
        if nums_len < 3:
            return list(ret)
        
        for i in range(nums_len - 2):
            result = ()
            for j in range(i+1, nums_len - 1):
                if i == j: continue
                for k in range(i+2, nums_len):
                    if i == k: continue
                    if j == k: continue
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        result = (nums[i], nums[j], nums[k])
                        ret.append(result)
        
        
        final_ret = []
        for i in range(len(ret)):
            final_ret_len = len(final_ret)
            for j in range(final_ret_len):
                if set(ret[i]) == set(final_ret[j]):
                    break
            else:
                final_ret.append(ret[i])
                
                    
        return final_ret


if __name__ == "__main__":
    solution = Solution()
    result = solution.threeSum([0, 0, 0, 0])
    print(result)
