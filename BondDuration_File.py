import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    df = 1 / (1 + r) ** t

    cf = np.full(n, c, dtype=float)
    cf[-1] += face

    pvcf = cf * df
    price = np.sum(pvcf)

    duration = np.sum(t * pvcf) / price / ppy
    return duration

print(getBondDuration(y=0.03, face=2000000, couponRate=0.04, m=10, ppy=1))



