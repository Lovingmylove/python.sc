#LeetCode-2(Add Two Numbers)
##Add Two Numbers
<pre>
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a signal digit. Add the two numbers and return it as a linked list.
</pre>
##Codes
<pre>
# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None
 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp, l1.val = divmod(l1.val + l2.val, 10)
        r = l1
        while(l1.next and l2.next):
            tmp, l1.next.val = divmod(l1.next.val + l2.next.val + tmp, 10)
            l1 = l1.next
            l2 = l2.next
        if l2.next:
            l1.next = l2.next
        while l1.next and tmp:
            tmp, l1.next.val = divmod(l1.next.val + tmp, 10)
            l1 = l1.next
        if tmp:
            l1.next = ListNode(1)
        return r
</pre>
##Why do it like this?
<pre>
for example, l1 = [2, 3], l2 = [4, 5, 6]
before while: l1 = [6, 3], tmp = 0
in the first while loop: l1 = [6, 8], tmp = 0, l1.next = None  ,l2.next != None
then break while and carried out "l1.next = l2.next"
final return r and now r = l1 = [6, 8, 6]
</pre>
##Is this solution ok?
<pre>
# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None
 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = 0
        r = l1
        while(l1 and l2):
            tmp, l1.val = divmod(l1.val + l2.val + tmp, 10)
            l1 = l1.next
            l2 = l2.next
        if l2:
            l1 = l2
        while l1 and tmp:
            tmp, l1.val = divmod(l1.val + tmp, 10)
            l1 = l1.next
        if tmp:
            l1 = ListNode(1)
        return r
</pre>
**Unfortunately, The solution is not so correct for some specific examples. for instance, l1 = [5], l2 = [5] and the output is [0] but the correct answer is [0, 1], why so?**   
**In the first solution, we judge the next node and caculate it. l1 will not be None and always exist. But in the second solution we judge the current node and caculate it then l1 becomes the next node and it may be None in some specific examples. So it's not so good.**
##Tips
<pre>
divmod(a,b): return (a//b, a%b)
</pre>
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                               Stay hungry, Stay foolish. ---Steve Jobs