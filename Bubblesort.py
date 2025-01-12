
# array = [45,34,63,45]
# n = len(array)
# for i in range(n):
#     for j in range(0 , n-i-1):
#         if array[j] > array[j+1]:
#             array[j] , array[j+1] = array[j+1] , array[j]
# print(array)


#Count the Number of Swaps   using bubblesort


# arr = [64, 34, 25, 12, 22, 11, 90]
# n = len(arr)
# swap_count = 0

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if arr[j] > arr[j + 1]:
#             # Swap the elements
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             swap_count += 1

# print(f"Sorted array: {arr}")
# print(f"Total number of swaps: {swap_count}")



# def array(xxx):
#     a = len(xxx)
#     for b in range(a):
#         for c in range(0,a-b-1):
#             if xxx[c] > xxx[c+1]:
#                 xxx[c] , xxx[c+1] = xxx[c+1] , xxx[c]
#     return xxx


# xxx = [4,1,6,3,9,2]
# answer = array(xxx)
# print(answer)


# def is_sort_or_sort(arr):
#     if all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)):
#         return arr
#     n = len(arr)
#     for k in range(n):
#         for m in range(0,n-k-1):
#             if arr[m] > arr[m+1]:
#                 arr[m] , arr[m+1] = arr[m+1] , arr[m]
#     return arr

# arr = [1,5,3,7,2,9]
# x = is_sort_or_sort(arr)
# print(x)


# def check(bubble):
#     n = len(bubble)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if len(bubble[j]) < len(bubble[j+1]):
#                 bubble[j] , bubble[j+1] = bubble[j+1] , bubble[j]
#     return bubble
# bubble = ['lucky','lisa','satrughna','dip']
# print(check(bubble))


# item = [(1,8),(3,1),(9,2),(8,3)]
# n = len(item)
# for i in range(n):
#     for j in range(n-i-1):
#         if item[j][1] > item[j+1][1]:
#             item[j] , item[j+1] = item[j+1], item[j]
    
# print(item)

# def sort_by_second_element(tuples):
#     n = len(tuples)
#     print("Initial List:", tuples)
#     # Bubble Sort based on the second element of each tuple
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if tuples[j][1] > tuples[j + 1][1]:  # Compare second elements
#                 tuples[j], tuples[j + 1] = tuples[j + 1], tuples[j]
#         print(f"After pass {i + 1}: {tuples}")
#     return tuples

# # Example Input
# input_tuples = [(1, 4), (2, 1), (3, 5), (4, 2)]

# # Sorting by the second element with visualization
# sorted_tuples = sort_by_second_element(input_tuples)

# # Final Output
# print("Sorted List:", sorted_tuples)



