#!/usr/bin/env python

import sys

def distance(s1,s2):

    n = len(s2)
    m = len(s1)

    # create cache table
    table = [['.' for j in range(n+1)] for i in range(m+1)]
    
    # initialize base cases
    begin_col = n-max(n-m,0)
    # if m > n
    # then we don't need to initialize any row
    # if m == n
    # then we initialize only the last one
    # if m < n
    # then we initialize from the difference
    for i in range(m+1):
        table[i][-1] = m-i
    for j in range(begin_col,n+1):
        table[-1][j] = n-j
    
    d = _distance(s1,s2,0,0,table)
    #print_table(table,s1,s2)
    return d    


def _distance(s1,s2,i,j,table):
    if table[i][j] != '.':
        return table[i][j]
    d_ins = _distance(s1,s2,i+1,j+1,table) + 1
    d_mod = _distance(s1,s2,i+1,j+1,table) + (0 if s1[i]==s2[j] else 1)
    d_rem = _distance(s1,s2,i  ,j+1,table) + 1
    table[i][j] = min(d_ins,d_mod,d_rem)
    return table[i][j]
    


def print_table(table,s1,s2):
    m = len(table)
    print(' ',s2,'*',sep='')
    for i in range(m):
        print(s1[i] if i < m-1 else '*',*table[i],sep='')


if __name__ == '__main__':
    print(distance('kitten','sitting'))
    print(distance('sitting','kitten'))
    print(distance('d','ojeda'))
