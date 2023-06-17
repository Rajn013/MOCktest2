#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Answer 1.

def sqrt(x):
    if x == 0:
        return 0
   
    guess = x
    while guess * guess >x:
        guess = (guess + x // guess) // 2
    
    return guess


# In[7]:


x = 4
result  = sqrt(x)
print(result)


# In[8]:


x = 8
result= sqrt(x)
print(result)


# In[20]:


#answer2.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        curr.next = ListNode(digit)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


# In[21]:


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next


# In[23]:


l1 = ListNode(0)

l2 = ListNode(0)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.val


# In[24]:


# Create the linked lists
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next


# In[ ]:




