import matplotlib.pyplot

def f(x):
    c=10
    return c if x<=c else x

print("{0} {1} {2}".format(f(3),f(88),f(12)))