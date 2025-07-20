import random
# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set 
# of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], 
# return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
# use triessss REMAINING
dict = []
def fill_dict(st):
    st2 = st.split(',')
    global dict
    for a in st2:
        dict.append(a)

def autocomplete1(st):
    global dict
    dict2= []
    for a in dict:
        if(a.find(st)!=-1):
            dict2.append(a)
    return dict2

# def autocomplete2(st):
#     global dict
fill_dict('dog, deer, deal')
print(autocomplete1('de'))

# This problem was asked by Amazon.
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, 
# you could climb any number from a set of positive integers X? 
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
# for part 1: recursion formed = no_ways(n) = no_ways(n-1) + no_ways(n-2)
# for part 2: recursion formed = no_ways(n)+ = no_ways(n-i) for i in X ; if (n-i)<0 return 0 REMAINING
X=[1, 3, 5]
ways_recur2 = 0
def no_ways_recur(n):
    if(n==1):
        return 1
    if(n==2):
        return 2 
    return no_ways(n-1) + no_ways(n-2)

def no_ways_recur2(remaining, lis):
    if(remaining<=1):
        return 1
    ways_t = 0
    for i in lis:
        if(remaining>=i):
            ways_t+=no_ways_recur2(remaining-i, lis)
    return ways_t

def no_ways_iter(n):
    ways_1 = 1
    ways_2 = 2
    for i in range(2, n):
        ways_2, ways_1 = ways_1 + ways_2, ways_2
    return ways_2

print(no_ways_iter(3))
print(no_ways_recur2(4, [1, 3, 5]))

# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring 
# that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k 
# distinct characters is "bcb".
def longest_substring(s, k):
    start = 0
    end = 0
    max_count = 0
    dict = {}
    for i in range(0, len(s)):
        end = i
        dict[s[i]]=1
        if(len(dict.keys())<=k):
            max_count+=1
        else:
            dict.pop(s[start])
            start+= 1
            max_count = max(max_count, end-start+1)
    return max_count
print(longest_substring('abcba', 2))

# This problem was asked by Google.
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.
# SOLUTION: all the points in the range of x[-1, 1] and y[0, 1] would be in a sq. of side 1
# and find if the point lies inside circle, then pi = 4 * point_inside_circle/point_inside_square
points_inside_circle = 0
points_inside_square = 0

def random_generator(lower, upper):
    return random.uniform(lower, upper)

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def generate(self):
        self.x = random_generator(-1, 1)
        self.y = random_generator(0, 1)

def check_point(point):
    if(point.x>=0 or point.x<=1):
        if(point.y**2<=(1-point.x**2)):
            return 1
    return -1

def monte_carlo():
    global points_inside_circle
    global points_inside_square
    for i in range(100):
        a = Point()
        a.generate()
        if(check_point(a)==1):
            points_inside_circle+=1
        points_inside_square+=1
    pi = 4.0*points_inside_circle/points_inside_square
    return pi

print('{0:.3f}'.format(round(monte_carlo(), 3)))

# This problem was asked by Facebook.
# Given a stream of elements too large to store in 
# memory, pick a random element from the stream with uniform probability

def choose(stream):
    random_element = None
    count = 0
    for (i in stream):
        if(count==0):
            random_element = i
        else:
            if(random.randint(0, count)==0):
                random_element = i
    return random_element