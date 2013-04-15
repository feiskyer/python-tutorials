#!/usr/bin/env python
from stack import Stack
    
digits = "0123456789ABCDE"

def baseConverter(decNumber, base):
    digits = "0123456789ABCDE"
    remstack=Stack()
    while decNumber>0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber=decNumber//base
    newstring=''
    while not remstack.isEmpty():
        newstring = newstring + digits[remstack.pop()]
    return newstring

def baseConverter2(decNumber, base):
    if decNumber<base:
        return digits[decNumber]
    else:
        return baseConverter2(decNumber//base,base) + digits[decNumber%base]

if __name__=='__main__':
    print baseConverter(1024, 2)
    print baseConverter2(1024, 2)
    print baseConverter(1024, 10)
    print baseConverter2(1024, 10)
    print baseConverter(1024, 8)
    print baseConverter(1024, 16)
