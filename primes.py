"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isItPrime(y):
    for i in range(2, int(y**0.5) + 1):
        if y % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError('Wrong input entered')
    list = []
    y = 1
    while(len(list) < number_of_primes):
        y += 1
        if isItPrime(y):
            list.append(y)
    return list
