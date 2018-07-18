
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda x, y: x)


def cdr(pair):
    return pair(lambda x, y: y)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
