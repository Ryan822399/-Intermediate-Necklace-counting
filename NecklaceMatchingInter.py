#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string

"""
Created on Thu May 21 14:20:51 2020

For the purpose of this challenge, a k-ary necklace of length n is a sequence of n letters chosen from k options, e.g. ABBEACEEA is a 5-ary necklace of length 9. Note that not every letter needs to appear in the necklace. Two necklaces are equal if you can move some letters from the beginning to the end to make the other one, otherwise maintaining the order. For instance, ABCDE is equal to DEABC. For more detail, see challenge #383 Easy: Necklace matching.

Today's challenge is, given k and n, find the number of distinct k-ary necklaces of length n. That is, the size of the largest set of k-ary necklaces of length n such that no two of them are equal to each other. You do not need to actually generate the necklaces, just count them.

For example, there are 24 distinct 3-ary necklaces of length 4, so necklaces(3, 4) is 24. Here they are:

AAAA  BBBB  CCCC
AAAB  BBBC  CCCA
AAAC  BBBA  CCCB
AABB  BBCC  CCAA
ABAB  BCBC  CACA
AABC  BBCA  CCAB
AACB  BBAC  CCBA
ABAC  BCBA  CACB
You only need to handle inputs such that kn < 10,000.

necklaces(2, 12) => 352
necklaces(3, 7) => 315
necklaces(9, 4) => 1665
necklaces(21, 3) => 3101
necklaces(99, 2) => 4950
The most straightforward way to count necklaces is to generate all kn patterns, and deduplicate them (potentially using your code from Easy #383). This is an acceptable approach for this challenge, as long as you can actually run your program through to completion for the above examples.

                                                                                                      Optional optimization
A more efficient way is with the formula:

necklaces(k, n) = 1/n * Sum of (phi(a) k^b)
    for all positive integers a,b such that a*b = n.
For example, the ways to factor 10 into two positive integers are 1x10, 2x5, 5x2, and 10x1, so:

necklaces(3, 10)
    = 1/10 (phi(1) 3^10 + phi(2) 3^5 + phi(5) 3^2 + phi(10) 3^1)
    = 1/10 (1 * 59049 + 1 * 243 + 4 * 9 + 4 * 3)
    = 5934
phi(a) is Euler's totient function, which is the number of positive integers x less than or equal to a such that the greatest common divisor of x and a is 1. For instance, phi(12) = 4, because 1, 5, 7, and 11 are coprime with 12.

An efficient way to compute phi is with the formula:

phi(a) = a * Product of (p-1) / Product of (p)
    for all distinct prime p that divide evenly into a.
For example, for a = 12, the primes that divide a are 2 and 3. So:

phi(12) = 12 * ((2-1)*(3-1)) / (2*3) = 12 * 2 / 6 = 4
If you decide to go this route, you can test much bigger examples.

necklaces(3, 90) => 96977372978752360287715019917722911297222
necklaces(123, 18) => 2306850769218800390268044415272597042
necklaces(1234567, 6) => 590115108867910855092196771880677924
necklaces(12345678910, 3) => 627225458787209496560873442940

https://www.reddup.co/r/dailyprogrammer/comments/g1xrun/20200415_challenge_384_intermediate_necklace

@author: ryanhennes
"""

#Creating alphabet to itterate through later
alphabets = string.printable
#print(alphabets)

# code solution credit to u/sunnyabd
def check(perms):
    counter = 0
    while counter < len(perms):
        letters = perms[counter]
        size = len(letters)
        letterDouble = letters+letters
        tempPerms = perms[counter+1:]
        for i in range(1, size):
            try:
                tempPerms.remove(str(letterDouble[i:(i+size)]))
            except:
                continue
        perms = perms[:counter+1] + tempPerms
        counter += 1
    #print(perms)
    return perms

#generating permutations recursively
def perms(letters, length, curr=[]):
    if length == 0:
        #yield returns the curr value but also preserves the state of the function
        yield curr
        return
    for i in alphabets[0:letters]:
        curr.append(i)
        yield from perms(letters, length-1, curr)
        curr.pop()

#takes in the number of letters starting from A (alpha), and the length of the necklace (length)
def necklaces(alpha, length):
    perm = list()
    # looping through each permutation generated
    for i in perms(alpha,length):
        perm.append("".join(map(str,i)))
    # checks
    return len(check(perm))
    
    
print(necklaces(2, 12))
print(necklaces(3, 7))
print(necklaces(9, 4))
print(necklaces(21, 3))
print(necklaces(99, 2))
    
    
