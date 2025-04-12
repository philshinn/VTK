from sys import version

print(version)

def execute(a, st):
    b = 42
    exec("b = {}\nprint('b:', b)".format(st))
    print(b)
a = 1.
execute(a, "1.E6*a")