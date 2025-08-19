import time

def time_complexity_example1(list):
    start_time = time.time()
    res= list[0] # O(1) - Constant time complexity
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")   
    return res

def time_complexity_example2(list,key):
    start_time = time.time()
    left=0
    right=len(list)-1
    while left <= right:  # O(n) - Linear time complexity
       mid= (left + right) // 2
       if list[mid] == key:
            end_time = time.time()
            print(f"Execution time for binary search if found: {end_time - start_time} seconds")
            print(f"Key {key} found at index {mid}")           
            return mid
       elif list[mid] < key:
            left = mid + 1
       else:
            right = mid - 1
    end_time = time.time()
    print(f"Execution time for binary search if not found: {end_time - start_time} seconds")
    return -1





def binary_search_recursive(arr, key, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, right)
    else:
        return binary_search_recursive(arr, key, left, mid - 1)



def linear_search(arr, key):
    for i in range(len(arr)):  # O(n) - Linear time complexity
        if arr[i] == key:
            return i
    return -1
a=[1, 2, 3, 4, 5]
time_complexity_example1(a)
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key=5
time_complexity_example2(b, key)

key1=0
time_complexity_example2(b, key1)


c=[2,3,5,8,10,12,20,30,50]

key3=18
res=binary_search_recursive(c, key3, 0, len(c) - 1)
if res == -1:
    print(f"Key {key3} not found in the list.")
else:
    print(f"Key {key3} found at index {res}.")

res2=linear_search(c, 30)
if res2 == -1:
    print(f"Key {30} not found in the list.")
else:
    print(f"Key {30} found at index {res2}.")