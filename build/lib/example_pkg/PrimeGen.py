def PrimeGen (x) :	
    for x in range (100):
        is_prime=True
        i=2
    while is_prime and i <x//2:
        if (x%i)==0:
           	is_prime=False
        i=i+1
    if is_prime==True:
        yield(x)

    