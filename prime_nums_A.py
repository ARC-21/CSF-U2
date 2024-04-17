# I swear, on my honor, I did not google any solutions, algorithms, or
# Python code related to this problem, or get another person to give me any
# solutions, algorithms, or Python code related to this problem. I solved it
# entirely by myself. -Arjun Chitla


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
