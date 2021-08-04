number = []
for x in range(1,100):
    for prime in range(2,x):
        if (x % prime) == 0:
            break
        elif(x % prime !=0) and (prime == x-1):
            number.append(x)
print(number)
