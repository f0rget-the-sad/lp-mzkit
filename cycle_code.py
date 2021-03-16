#!/usr/bin/env python3

def bit_len(x):
    # use `format` instead of `bin` to avoid `0b` prefix
    return len(format(x, 'b'))

def reminder(num, div):
    div_len = bit_len(div)
    res = num << (div_len - 1)
    print(f"{res:b}/{div:b}")

    shift_len = bit_len(res) - div_len
    n_of_iter = 0
    while shift_len >= 0:
        curr_div = div << shift_len
        res ^= curr_div

        print(" " * n_of_iter + f"{curr_div:b}")
        print(" " * n_of_iter + "-" * div_len)
        n_of_iter += 1

        print(" " * n_of_iter + f"{res:b}")
        shift_len = bit_len(res) - div_len
    return res

def cycle_code(num, div):
    return reminder(num, div) | num << (bit_len(div) - 1)

num1 = 0b1101
div1 = 0b1011
code = cycle_code(num1, div1)
print(f"{code:b}")

print("Verification")
r = reminder(code, div1)
assert r == 0, "division of cycle code should give 0"
