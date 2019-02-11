class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [0,0]
        for i in range(0,len(nums)-1):
            res[0] = i
            for j in range(i+1,len(nums)):
                res[1] = j
                if nums[res[0]] + nums[res[1]] == target:
                    return res
    
    def twoSumDict(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(0,len(nums)):
            if dict.get(target - nums[i]) is None:
                dict[nums[i]] = i
            else:
                return [dict.get(target - nums[i]),i]
                

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums,target))
    print(solution.twoSumDict(nums,target))
