# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 23:32:57 2023

@author: EricSyu
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class Solution:
    
    def __init__(self):
        self.base = 10
    
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        # fill zero
        addzeronum = abs(len(l1) - len(l2))
        if len(l1) > len(l2):
            for _ in range(addzeronum):
                l2.append(ListNode(0))
        else:
            for _ in range(addzeronum):
                l1.append(ListNode(0))
        
        # calculate answer
        ans = []
        iternum = len(l1) if len(l1) >= len(l2) else len(l2)
        carry = 0
        for idx in range(iternum):
            tmp = l1[idx].val + l2[idx].val
            x = (tmp + carry) % self.base
            carry = (tmp + carry) // self.base
            ans.append(ListNode(x))
            if idx == iternum-1 and carry != 0:
                ans.append(ListNode(carry))
        
        # write address
        for idx, node in enumerate(ans[:-1]):
            node.next = ans[idx+1]
        
        return ans


if __name__ == "__main__":
    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]
    
    # c = ListNode(3)
    # b = ListNode(4, c)
    # a = ListNode(2, b)
    # l1 = [a, b, c]
    
    # f = ListNode(4)
    # e = ListNode(6, f)
    # d = ListNode(5, e)
    # l2 = [d, e, f]
    
    # a = ListNode(0)
    # l1 = [a]
    
    # b = ListNode(0)
    # l2 = [b]
    
    g = ListNode(9)
    f = ListNode(9, g)
    e = ListNode(9, f)
    d = ListNode(9, e)
    c = ListNode(9, d)
    b = ListNode(9, c)
    a = ListNode(9, b)
    l1 = [a, b, c, d, e, f, g]
    
    k = ListNode(9)
    j = ListNode(9, k)
    i = ListNode(9, j)
    h = ListNode(9, i)
    l2 = [h, i, j, k]
    
    sol = Solution()
    c = sol.addTwoNumbers(l1, l2)
    for i in c:
        print(i.val, end="")
    
    
    
    
    
    