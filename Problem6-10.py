# This problem was asked by Google.

# An XOR linked list is a more memory efficient doubly linked list. 
# Instead of each node holding next and prev fields, it holds a field named both, 
# which is an XOR of the next node and the previous node. Implement an XOR linked list; 
# it has an add(element) which adds the element to the end, and a get(index) which returns 
# the node at index.
class Xor_Node:
    def __init__(self, value):
        self.val = value
        self.both = 0
    
class Xor_ll():
    def __init__(self):
        self.head=Xor_Node(None)
        self.tail=Xor_Node(None)
    def add(element):
        node = Xor_Node(element)
        if(self.head.val==None):
            self.head = self.tail = node
        node.both = 0 ^ get_pointer(self.head)
        temp = self.head.both ^ 0
        self.head.both = node.both ^ temp
    def get(index):
        # todo
a_x = Xor_Node(2)
b_x = Xor_Node(3)
# a_x, b_x = xor(a_x, b_x)
print(get_pointer(a_x))

# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of 
# ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed
# recurrence = no of ways(i) = (no of ways(i-1) + check if i is a char) + (no of ways(i-2)+ check if last 2 digits are valid)
def no_ways(st):
    arr = [0 for i in range(len(st)+1)]
    arr[0] = 1
    if int(st[0])==0:
        arr[1] = 0
        return 0
    else:
        arr[1]=1
    for i in range(2, len(st)+1):
        if(int(st[i-1])!=0):
            arr[i]+=arr[i-1]
        if(int(st[i-2:i])>10 and int(st[i-2:i])<26):
            arr[i]+=arr[i-2]
    return arr[len(st)]
print(no_ways('11'))

# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def is_unival(root):
    return helper(root, root.value)
def helper(root, value):
    if(root==None):
        return True
    if(root.value == value):
        if(helper(root.left, value) and helper(root.right, value)):
            return True
    return False
def count_unitree(root):
    if(root==None):
        return 0
    trees = count_unitree(root.left)+count_unitree(root.right)
    return trees+1 if is_unival(root) else trees

# def count_unitree_norecurse(root):
#     if(root==None):
#         return 0
a = Node(1)
b = Node(1)
c = Node(1, a, b)
d = Node(0)
e = Node(0, c, d)
f = Node(1)
root = Node(0, f, e)
print(count_unitree(root))

# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum 
# of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?
# recurrence -> sum(n) = max(sum(n-2)+value, sum(n-1))
def max_sum(arr):
    dp = [0 for ele in range(len(arr))]
    dp[0] = arr[0]
    dp[1] = max(dp[0], arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-2]+arr[i], dp[i-1])
    return dp[len(arr)-1]
print(max_sum([2,4,6,2,5]))

# This problem was asked by Apple.
# Implement a job scheduler which takes in a function f and an integer n, 
# and calls f after n milliseconds