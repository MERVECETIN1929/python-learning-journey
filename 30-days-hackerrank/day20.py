#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    swap_count = 0

    for i in range(n):
        for j in range(n-1-i):

            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]

                swap_count += 1

    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]}")

    print(f"Last Element: {a[n-1]}")
