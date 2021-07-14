#!/usr/bin/env python

import tools

def problem_001():
  multiples_list = tools.list_multiples(1000, [3, 5])
  return sum(multiples_list)

def problem_002():
  list = tools.fib_list(4000000)

  even_sum = 0
  for num in list:
    if num % 2 == 0:
      even_sum += num

  return even_sum

def problem_003():

  return tools.prime_factorization(600851475143)

def problem_025():
  index = 0
  term = 0
  length = 0  

  while length < 1000:
    index += 1
    term = tools.fibonacci(index)
    length = len(str(term))

  return index