a = float(input('Enter the number:'))
if a < 2:
    print('Is not prime number')
else :
    prime = True
    
    for i in range(2,a):
        if a % i == 0:
            prime = False
            break
if prime:
    print(a, 'is the prime number')
else :
    print(a, 'is not the prime number')