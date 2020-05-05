# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:23:57 2020

@author: Linh
"""

def fib(n):
    '''Computes the nth Fibonacci number.'''
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)