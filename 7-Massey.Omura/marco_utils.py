import sys
import os
import math


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]




def gcd(a,b):
    """ Return GCD between a and b """

    while b != 0:
        a, b = b, a % b

    return a


def lcm(x, y):
    """ Return LCM between x and y"""

    if x > y:
        greater = x
    else:
        greater = y

    while(True):

        if((greater % x == 0) and (greater % y == 0)):
               a = greater
               break
        greater += 1
    return a
