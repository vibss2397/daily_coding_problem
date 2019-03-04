# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
def min_rooms(arr):
    start = sorted([inp[0] for inp in arr])
    end = sorted([inp[1] for inp in arr])
    i, j = 0, 0
    rooms = 0
    max_rooms = 0
    n = len(arr)
    while i<n and j<n:
        if(start[i]<end[j]):
            rooms+=1
            i+=1
        elif(start[i]>end[j]):
            rooms-=1
            j+=1
        max_rooms = max(rooms, max_rooms)
    for a in range(i, n):
        rooms+=1
    for b in range(j, n):
        rooms-=1
    max_rooms = max(rooms, max_rooms)
    return max_rooms
    
print(min_rooms([(30, 75), (0, 50), (60, 150)]))

# This problem was asked by Microsoft.
# Given a dictionary of words and a string made up of those words (no spaces), 
# return the original sentence in a list. If there is more than one possible 
# reconstruction, return any of them. If there is no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and 
# the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] 
# or ['bedbath', 'and', 'beyond'].
