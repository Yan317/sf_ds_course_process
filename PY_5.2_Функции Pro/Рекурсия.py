# Функия факториала
def factorial(n):
    if n == 0: return 1
    if n == 1: return 1
    return n * factorial(n-1)

from time import time
import sys
sys.setrecursionlimit(1000000000)

a = time()
for i in range(100):
    factorial(1000)
b = time()
print(b-a)

