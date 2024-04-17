'''Weird Base 5
Problem:
You should know by now how base 5 works. Allow me to introduce you to... weird base 5. The place values are the
same, but the digits are not. Instead of having the digits 0, 1, 2, 3, and 4, weird base 5 has a different set of digits, the
digits 2, 1, 0, - (minus) and = (double minus). If there is a - (minus) in a certain place, you subtract one of that place
value. If there is a = (double minus) in a place, you subtract two of that place value.
For example, we could write the number 1=-2 in weird base 5. The place values would be the same as normal base 5, so
this means we’d have:
 1 in the 125s place
 = (double minus) in the 25s place
 - (minus) in the 5s place
 2 in the 1s place
So this would be the number 125 – 50 – 5 + 2 = 72.
Your challenges:
 (1 point) Write a program that will convert a weird base 5 number to the normal base 10 representation of that
same number.'''


og_num = input("Enter a number in weird base 5: ")
base_10 = 0
num_of_digits = len(og_num)
for i in range(num_of_digits):
    num_of_digits -= 1
    if og_num[num_of_digits] == "-":
        base_10 -= 5**i
    elif og_num[num_of_digits] == "=":
        base_10 -= 2*5**i
    else:
        base_10 += int(og_num[num_of_digits])*5**i
print("In base 10, it's: " + str(base_10))
