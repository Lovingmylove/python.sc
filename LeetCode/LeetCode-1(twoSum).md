#LeetCode-1(Two Sum)
**LeetCode OJ is a platform for preparing technical coding interviews. It has more than 190 questions and today I will try to solve them with python. Good luck!**
##Two Sum
<pre>
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
</pre>
##Codes
<pre>
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if d.has_key(n):
                return (d[n], i)
            else:
                d[target-n] = i
        return (0,0)
</pre>
##Why do it like this?
<pre>
d: type dictionary
i: the indices of nums
n: the content of nums
for example, nums = [2,3,4,5], target = 9
in the first loop: d.has_key(2) == Flase # Now d is {7:0}
in the second loop: d.has_key(3) == Flase # Now d is {7:0, 6:1}
in the third Loop: d.has_key(4) == Flase # Now d is {7:0, 6:1, 5:2}
in the final Loop: d.has_key(5) == Ture # Now d(5)=2, i=3
So, the answer is (2, 3)
</pre>
##One more solution
<pre>
import numpy as np
def twoSum(nums, target):
    result = []
    numsIndices = np.argsort(nums)
    for i in range( 0, len(nums)):
        for j in range(i+ 1, len(nums)):
            if nums[numsIndices[i]] + nums[numsIndices[j]] == target:
                result.append(numsIndices[i])
                result.append(numsIndices[j])
                break
        if result != []:
            break
    return result
</pre>
##Tips
<pre>
argsort: return the indices of a sorted list
for every i, traversal j until the condition "nums[numsIndices[i]] + nums[numsIndices[j]" is ture, then break.
</pre>
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                            Stay hungry, Stay foolish. ---Steve Jobs