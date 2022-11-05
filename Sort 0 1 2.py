'''
CODE
'''

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    arr1 = []
    arr2 = []
    arr3 = []
    for p in range(len(arr)):
        if arr[p] == 0:
            arr1.append(0)
        elif arr[p] == 1:
            arr2.append(1)
        else:
            arr3.append(2)
    sorted = arr1 + arr2 + arr3
    for i in range(len(sorted)):
        arr[i] = sorted[i]
               
      
