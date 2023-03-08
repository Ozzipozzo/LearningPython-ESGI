import math

def cube(x):
    return x ** 3

def volumeSphere(r):
    v = (4 / 3) * math.pi * cube(r)
    return v
