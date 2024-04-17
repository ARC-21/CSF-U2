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
