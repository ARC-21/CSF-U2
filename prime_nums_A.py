# I swear, on my honor, I did not google any solutions, algorithms, or
# Python code related to this problem, or get another person to give me any
# solutions, algorithms, or Python code related to this problem. I solved it
# entirely by myself. -Arjun Chitla

'''
Problem:
Determining whether or not a number is prime is a great algorithm to figure out on your own! If you’ve forgotten what
a prime number is, feel free to ask your teacher.
You should also know that “twin prime” numbers are prime numbers that are only a distance of 2 apart. For example,
17 and 19 are a pair of twin prime numbers, as are 71 and 73, but 19 and 23 are too far apart.
Your challenges:
 Figure out a way to write a function that takes a number and returns True if that number is prime, and False if
that number isn’t prime. Then, use your is_prime function and write a new function that will take a number, n,
and find the number of pairs of twin primes less than n. For instance, there are 4 pairs of twin primes less than
20: 3 and 5, 5 and 7, 11 and 13, 17 and 19.
 (1 point) If your code can generate the number of pairs of twin primes less than 10,000 in less than 10 seconds,
you get one point. (You may not store this information in a .txt file or hardcoded within your .py file; your code
has to generate it from scratch.)
 (1 point) If your code can generate the number of pairs of twin primes less than 1,000,000 in less than 10
seconds, you get an additional point for a total of 2. (You may not store this information in a .txt file or
hardcoded within your .py file; your code has to generate it from scratch.)
'''

import math

def is_prime(n):
    fcount = 0
    i = 2
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def prime_twins(n):
    p = 2
    pcount = 0
    prev_prime = 0
    while p < n:
        #print(p)
        #print("prev " + str(prev_prime))
        if is_prime(p):
            #print("ding!")
            if p - prev_prime == 2:
                #print("DING!")
                pcount += 1
            prev_prime = p
        #print(prev_prime)
        p += 1
    return pcount-1

n = prime_twins(1000000)
print(n)
