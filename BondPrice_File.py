import numpy as np

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    df = 1 / (1 + r) ** t

    cf = np.full(n, c, dtype=float)
    cf[-1] += face

    price = np.sum(cf * df)
    return price
print(getBondPrice(y=0.03, face=2000, couponRate=0.04, m=10, ppy=1))
