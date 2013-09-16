##maxnumber = int(raw_input("please enter the highest number you want to check: "))
a = 10**4

maxnumber = a
print maxnumber

primes = []
primes.append(2)
for i in range (maxnumber):
    Prime = True
    if i > 2:
        for j in primes:
            if i%j == 0:
                Prime = False
        if Prime == True :
            primes.append(i)
print primes
print len(primes)

    

