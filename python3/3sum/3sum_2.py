from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums_len = len(nums)
        
        if nums_len < 3:
            return list(ret)
        
        print("nums = {}".format(nums))
        for i in range(nums_len - 2):
            result = ()
            print("nums[i = {}] = {}".format(i, nums[i]))
            for j in range(i+1, nums_len - 1):
                if i == j: continue
                print("nums[j = {}] = {}".format(j, nums[j]))
                for k in range(i+2, nums_len):
                    if i == k: continue
                    if j == k: continue
                    print("nums[k = {}] = {}".format(k, nums[k]))
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        result = (nums[i], nums[j], nums[k])
                        print("add result = [{} = {}, {} = {}, {} = {}] to ret".format(i,nums[i], j,nums[j], k,nums[k]))
                        if len(ret) == 0: 
                            ret.append(result)
                            continue
                        for l in ret:
                            if set(l) == set(result):
                                break
                        else:
                            ret.append(result)
        
                
        print("ret = {}".format(ret))
        return ret


if __name__ == "__main__":
    solution = Solution()
    result = solution.threeSum([0, 0, 0, 0])
    print(result)
