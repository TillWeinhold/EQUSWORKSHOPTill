x = int(input ("Enter number :") )
print(x) 
    is_prime=True
    i=2
    while is_prime and i <x//2:
        if (x%i)==0:
            is_prime=False
        i=i+1
    if is_prime==True:
        outcome_stg=('is a prime number')
    else:
        outcome_stg=('is not a prime number')
    print('{}, {}'.format(x, outcome_stg))