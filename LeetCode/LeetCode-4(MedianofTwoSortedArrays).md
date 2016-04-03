#LeetCode-4(Median of Two Sorted Arrays)
##Median of Two Sorted Arrays
**There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).**
##Codes
<pre>
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l=len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0


    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)
</pre>
##Is this way better enough?
**The answer is no. It wasted too much time.**   
![](https://github.com/Lovingmylove/python.sc/raw/master/LeetCode/Median_of_Two_Sorted_Arrays_1.png)
##Is their a rude but simple solution?
<pre>
def findMedianSortedArrays(self, A, B):
      """
      :type nums1: List[int]
      :type nums2: List[int]
      :rtype: float
      """
      if len(A) > len(B):
         A, B = B, A
      if not A:
         return self.findMedian(B)
      else:
         C = A + B
         nums = sorted(C)
         return self.findMedian(nums)
      def findMedian(self, num):
         length = len(num)
         if length%2 == 1:
            return num[length//2]
         else:
            return (num[length//2-1] + num[length//2])/2.0
</pre>
![](https://github.com/Lovingmylove/python.sc/raw/master/LeetCode/Median_of_Two_Sorted_Arrays_2.png)
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                              Stay hungry, Stay foolish. ---Steve Jobs
