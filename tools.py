#!/usr/bin/env python

import math

def list_multiples(max_num, list_factors):
  list = []
  for num in range(max_num):
    for factor in list_factors:
      if num % factor == 0:
        list.append(num)
        break

  return list


def fib_list(max_number):
  list = [0, 1]
  
  while list[-1] < max_number:
    list.append(list[-2] + list[-1])

  if list[-1] > max_number:
    list.pop(-1)
  return list

# 
# Fast doubling Fibonacci algorithm (Python)
# 
# Copyright (c) 2015 Project Nayuki. Public domain.
# https://www.nayuki.io/page/fast-fibonacci-algorithms
# 


# (Public) Returns F(n).
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)


def prime_factorization(number):
  list = []

  upper_bound = math.floor(math.sqrt(number))

  for factor in range(2, upper_bound):
    while number % factor == 0:
      number /= factor
      list.append(factor)


  return list