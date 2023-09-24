from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums is atleast len = 2
        # only one valid answer
        # requirement = time complexity < O(n^2)

        # O(n^2) solution
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # O(n) solution Beats 66.67%of users with Python3
        # O(n) memory Beats 47.59%of users with Python3
        # initialize a dictionary
        dictionary = {}
        # loop through the list
        for i in range(len(nums)):
            # check if another element that with nums[i] will equal target
            if target - nums[i] in dictionary:
                return [dictionary[target - nums[i]], i]
            # insert elements of the list in the dictionary as keys, index as value
            else:
                dictionary[nums[i]] = i

        # is it possible to make it more efficient in terms of space, time - not really
        # we can use enumerate when looping through the list so we have i, nums[i] -cleaner code
        # we can possibly use defaultdict from collections import defaultdict

        # from collections import defaultdict
        # def twoSum(nums, target):
        #     # initialize a defaultdict with a default value of -1
        #     dictionary = defaultdict(lambda: -1)

        #     for i, num in enumerate(nums):
        #         complement = target - num

        #         # Check if the complement exists in the dictionary.
        #         if dictionary[complement] != -1:
        #             return [dictionary[complement], i]

        #         # Insert elements of the list in the dictionary as keys, index as value.
        #         dictionary[num] = i
