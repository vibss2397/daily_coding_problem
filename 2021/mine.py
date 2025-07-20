def func(arr):
    start = 0
    end = len(arr)
    counter = 0
    while(start<end):
            ele = arr[start]
            if(ele==0):
                for i in range(end-1, start, -1):
                    arr[i] = arr[i-1]
                start+=2
                print(arr)

            else:
                print(arr[start], 'here')
                start = start + 1

func([1,0,2,3,0,4,5,0])