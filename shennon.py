#!/usr/bin/env python3
import sys

data = [10, 8, 6, 5, 4, 3]
# data = [22, 20, 16, 16, 10, 10, 4, 2]
# data = [30, 20, 10, 8, 8, 7, 7]
# data = [60, 30, 20, 15, 5, 5]

data = sorted(data, reverse=True)
codes = [""] * len(data)

def divide(data, offset):
    if not data or len(data) == 1:
        return
    min_diff = sys.maxsize
    n = 0
    for i in range(1, len(data)):
        curr_diff = abs(sum(data[:i]) - sum(data[i:]))
        if min_diff > curr_diff:
            n = i
            min_diff = curr_diff

    print(data[:n])
    print(data[n:])
    print("=====")
    for i in range(len(data[:n])):
        codes[offset + i] += "1"
    for i in range(len(data[n:])):
        codes[n + offset + i] += "0"
    divide(data[:n], offset)
    divide(data[n:], offset + n)

divide(data, 0)
for n, d_el in enumerate(data):
    print("{}\t{}".format(d_el, codes[n]))
