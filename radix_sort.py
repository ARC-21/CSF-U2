def counting_sort(nums, digit):

    c_array = [0]*10
    
    for i in range(len(nums)):
        dig = (nums[i] // digit) % 10
        c_array[dig] += 1

    for i in range(1,10):
        c_array[i] += c_array[i-1]

    new_array = [0] * len(nums)
    index = len(nums)-1

    while index >= 0:
        num = nums[index]
        dig = (num // digit) % 10
        c_array[dig] -= 1
        new_array[c_array[dig]] = num
        index -= 1
        
    return new_array

def radix_sort(nums):

    mx = max(nums)
    exp = 0
    
    while 10**exp <= mx:
        exp += 1
        
    digit = 1
    new_array = nums
    
    for i in range(exp):
        new_array = counting_sort(new_array, digit)
        digit *= 10
        print(new_array)
   
radix_sort([2,10,0,60,102,9,9,7400,534,7862,321])
