#LeetCode-3(Longest Substring Without Repeating Characters)
##Longest Substring Without Repeating Characters
**Given a String, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which length is 3.**
##Codes
<pre>
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        max_length = 0
        for c in s:
            if c not in substring:
                substring += c
            else:
                max_length = max(max_length,len(substring))
                substring = substring[substring.find(c)+1:] + c
        return max(max_length,len(substring))
</pre>
##Why do it like this?
<pre>
take s = "pwwkew" for example
in the first loop: substring = "p", max_length = 0
in the second loop: substring = "pw", max_length = 0
in the third loop: if is not satisfied, then max_length = 2, substring = "w"
in the fourth loop: substring = "wk",  max_length isn't change
in the fifth loop: substring = "wke", max_length isn't change.
in the sixth loop: if is not satisfied, max_length = 3, substring = "kew"
finally, return max(max_length, len(substring)) = 3
</pre>
##One more solution
<pre>
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        r, record, slow = 0, {}, 0
        
        for i, char in enumerate(s):
            if char not in record or record[char] < slow:
                r = max(r, i - slow + 1)
            else:
                slow = record[char] + 1
            record[char] = i
        return r
</pre>
**It has the same principle with the first solution except using a dict.**
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                              Stay hungry, Stay foolish. ---Steve Jobs