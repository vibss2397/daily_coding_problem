# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

#naive solution would be a nested loop and to check if list[i]+list[j]==k; for every i, for every j
#improved = O(n) time + O(n) space
def add(list, sum):
    dict = {}
    for a in list:
        if((sum-a) in dict):
            return True
        if(not a in dict):
            dict[a]=1
        else:
            dict[a]+=1
    return False
print(add([10, 15, 3, 7], 17))

# Problem #2
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?
# Naive Solution
def func(arr):
    prod = 1
    for num in arr:
        prod*=num
    for i in range(len(arr)):
        arr[i]=prod//arr[i]
    return(arr)
print(func([1, 2, 3, 4, 5]))
#Follow-up : for no division, can use log tho cuz log(a/b)=log(a)-log(b) :P or:
def func2(arr):
    n = len(arr)
    left = [1]*n
    right = [1]*n
    for i in range(1, n):
        left[i] = left[i-1]*arr[i-1]
        right[-i-1] = right[-i]*arr[i]
    dic = [0]*n
    for i in range(n):
        dic[i] = left[i]*right[i]
    return dic
print('follow up')
print(func([1, 2, 3, 4, 5]))

# This problem was asked by Google.
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
str = ''
def serialize(node):
    global str
    if(node==None):
        str+='/,'
        return
    str+=node.val+','
    serialize(node.left)
    serialize(node.right)

def deserialize(str):
    def func_de():
        val = next(vals)
        if(val=='/'):
            return None
        node = Node(val)
        node.left = func_de()
        node.right = func_de()
        return node
    arr=str.split(',')
    vals = iter(arr)
    return func_de()
node = Node('root', Node('left', Node('left.left')), Node('right'))
serialize(node)
print(str)
assert deserialize(str).left.left.val == 'left.left'