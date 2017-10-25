#!/usr/bin/env python
import math
import random
import sys
num_passwords = 1
length = 15;

if len(sys.argv) >= 2:
	num_passwords = sys.argv[1]
if len(sys.argv) >= 3:
	length = sys.argv[2]
num_passwords = int(num_passwords)
length = int(length)

chars_l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chars_u = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
syms = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','<','.','>','/','?']
nums = [0,1,2,3,4,5,6,7,8,9]
chars = [chars_l, chars_u, nums, syms]
passwords = []
final = ""

def select_random():
	r = random
	rr = r.randint(0,len(chars)-1)
	ss = r.randint(0,len(chars[rr])-1)
	return chars[rr][ss]

for x in xrange(num_passwords):
	for i in xrange(length):
		final = final + str(select_random())
	passwords.append(final)
	final = ""

for password in passwords:
	print password
