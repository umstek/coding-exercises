#!/bin/python

# Complete the function below.


def  maxXor( l,  r):
  return (max([i^j for i in range(l, r+1) for j in range(i, r+1)]))

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

