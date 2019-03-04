# This problem was asked by Twitter.
# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.
class Log:
    def __init__(self, n):
        self.n = n
        self.circular = [None]*n
        self.current = 0
    def record(self, order_id):
        self.circular[self.current] = order_id
        self.current+= 1
        if(self.current == self.n):
            self.current = 0

    def get_last(self, i):
        if(self.current-i>=0):
            return self.circular[self.current-i]
        else:
            i = i-self.current
            return self.circular[self.n-i]
    def get(self):
        return self.circular
log = Log(100)
log.record('0x2sf346')
log.record('2233as')
print('q16 '+log.get_last(2))

# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google
# Suppose we represent our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory 
# subdir2 containing a file file.ext.
# 
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. 
# subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
# subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# We are interested in finding the longest (number of characters) absolute path to a file 
# within our file system. For example, in the second example above, the longest 
# absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 
# (not including the double quotes).
# Given a string representing the file system in the above format, 
# return the length of the longest absolute path to a file in the abstracted file system. 
# If there is no file in the system, return 0.
# Note:
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.
class Node:
    def __init__(self, val, is_folder, parent = None):
        self.val = val
        if(is_folder):
            self. children = []
        self.parent = parent
    def add_child(self, child):
        self.children.append(child)

def process_string(string):
    temp_arr = string.split('\n')
    str = ''
    max_t = 0
    max_t_index = 0
    str+=temp_arr[0]
    l = len(temp_arr)


# This problem was asked by Google.
# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place 
# and you do not need to store the results. You can simply print them out as you compute them.
print('q18')
from collections import deque
def max_values(n, k, inp):
    de = deque()
    for i in range(k):
        while de and inp[i]>=inp[de[-1]]:
            de.pop()
        de.append(i)
    for i in range(k, n):
        print(inp[de[0]])
        while de and de[0]<=i-k:
            de.popleft()
        while de and inp[i]>=inp[de[-1]]:
            de.pop()
        de.append(i)
    print(inp[de[0]])
max_values(6, 3, [10,5,2,7,8,7])

# This problem was asked by Facebook.
# A builder is looking to build a row of N houses that can be of K different colors. 
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the 
# nth house with kth color, return the minimum cost which achieves this goal.

# A builder is looking to build a row of N houses that can be of K different colors. 
# He has a goal of minimizing cost while ensuring that no two neighboring houses are 
# of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build 
# the nth house with kth color, return the minimum cost which achieves this goal
# def color_houses(n, k, matrix):
#     dp = [[float(inf) for i in range k] for j in range(2)]
#     for i in range(k):
#         dp[0][i] = matrix[0][i]
#     for i in range(n):
#         min_color = float('inf')
#         second_min_color = float('inf')
#         color = None
#         for j in range(k):
#             dp[1][j] =

# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the intersecting node. 
# The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
print('q20')
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
    def add_next(self, head, val):
        while(not head.next==None):
            head = head.next
        temp = Node(val)
        head.next = temp
def length(head):
    if(head==None):
        return 0
    return 1+length(head.next)
def check_node(head1, head2):
    diff = length(head1)-length(head2)
    if(diff>0):
        for i in range(diff):
            head1 = head1.next
    else:
        for i in range(abs(diff)):
            head2 = head2.next
    while(head1.val!=head2.val):
        head1 = head1.next
        head2 = head2.next
    return head1

head = Node(3)
head.add_next(head, 7)
head.add_next(head, 8)
head.add_next(head, 10)

head2 = Node(99)
head2.add_next(head2, 1)
head2.add_next(head2, 8)
head2.add_next(head2, 10)
print(check_node(head, head2).val)