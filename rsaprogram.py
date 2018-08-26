from math import *
import sys
# Functions
#Function to check prime
def checkPrime(number):
    count = 0;
    for i in range(2,number):
        if number%i ==0:
            count = count +1;
        if count>1:
            print(number," is not a prime")
            sys.exit()
#Function to calculate coprime
def coprime(value):
    count = 1;
    for i in range(2,value):
        if gcd(i,value)==1:
            if count<3:
                count=count+1;
                continue;
            return i;

#Function to find Modular Multiplicative Inverse
def mmi(a,base):
    for i in range(2,base):
        if (a*i)%base ==1:
            return i;

#Main execution
def start():
    p = int(input("Enter prime number: "))
    q = int(input("Enter prime number: "))
    checkPrime(p)
    checkPrime(q)
    n=p*q
    gcd_value =gcd(p-1,q-1)
    phi =int((p-1)*(q-1)/gcd_value)
    e = coprime(phi)
    d = mmi(e,phi)
    return [e,d,n];
