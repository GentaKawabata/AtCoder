
"""
逆元を求める
「拡張 Euclid の互除法を用いる方法」らしい
O(log p)　(p: 法)
"""
def mod_inv(a: int, mod: int):
    b = mod
    u = 1
    v = 0

    while b > 0:
        t = int(a / b)
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    
    u %= mod
    if u < 0:
        u += mod
    
    return u
