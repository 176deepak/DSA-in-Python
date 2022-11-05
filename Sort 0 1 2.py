'''
CODE
'''

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    zero = []
    one = []
    two = []
    for p in range(len(arr)):
        if arr[p] == 0:
            zero.append(0)
        elif arr[p] == 1:
            one.append(1)
        else:
            two.append(2)
    sorted = zero + one + two
    for i in range(len(sorted)):
        arr[i] = sorted[i]
               
      
