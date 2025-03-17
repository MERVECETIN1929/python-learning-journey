#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#


def bitwiseAnd(N, K):
    # Write your code here
    bigger_and = 0
    if K-1 & K == K-1:
        return K-1
    for i in range(1, N):
        for j in range(i+1, N):
            and_result = i & j
            if and_result > bigger_and and and_result < K:
                bigger_and = and_result
    return bigger_and


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)
        print(res)
