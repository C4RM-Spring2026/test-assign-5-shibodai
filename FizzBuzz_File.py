import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    out = np.array(nums, dtype=object)

    m3 = (nums % 3 == 0)
    m5 = (nums % 5 == 0)

    out[m3] = "fizz"
    out[m5] = "buzz"
    out[m3 & m5] = "fizzbuzz"

    return out.tolist()
