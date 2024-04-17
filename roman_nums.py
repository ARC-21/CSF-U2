'''I swear, on my honor, I did not google any solutions, algorithms, or Pythom
code related to this problem, or get another person to give me solutions,
algorithms or Python code related to this problem. -Arjun Chitla

Problem:
Write a program that will take any valid (not necessarily minimal) roman numeral as an input, and will
print the base 10 representation of that number as well as the minimal roman numeral representation of that
number.'''

og_num = input("Enter a number in roman numerals: ")
og_num_split = [*og_num]
for i in range(len(og_num_split)):
    if og_num_split[i] == "I":
        og_num_split[i] = 1
    elif og_num_split[i] == "V":
        og_num_split[i] = 5
    elif og_num_split[i] == "X":
        og_num_split[i] = 10
    elif og_num_split[i] == "L":
        og_num_split[i] = 50
    elif og_num_split[i] == "C":
        og_num_split[i] = 100
    elif og_num_split[i] == "D":
        og_num_split[i] = 500
    else:
        og_num_split[i] = 1000
        
for j in range(1, len(og_num_split)):
    if og_num_split[j] > og_num_split[j-1]:
        og_num_split[j] = og_num_split[j]-og_num_split[j-1]
        og_num_split[j-1] = 0

def find_max(nums, n):
    index = 0
    while nums[index] <= n:
        index += 1
    return index-1

base_10 = sum(og_num_split)
print("Base 10 representation of " + og_num + " is: " + str(base_10))
nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

def match(n, nums):
    roman_nums = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM']
    return roman_nums[nums.index(n)]
indexes = []
count = -1
while base_10 != 0:
    indexes.append(find_max(nums,base_10))
    count += 1
    base_10 -= nums[indexes[count]]

roman_num = ''
for n in indexes:
    roman_num += match(nums[n],nums)

print("Minimal roman numeral representation of " + og_num + " is: " + roman_num)
