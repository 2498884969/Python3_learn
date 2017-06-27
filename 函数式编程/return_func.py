def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs



def count():
    def f(j):
        def g():
            return j*j
        return g
    fs= []
    for i in range(1,4):
        fs.append(f(i))
    return fs