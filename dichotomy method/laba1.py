class Counter:
    def __init__(self, func):
        self.counter = 0
        self.func = func

    def __call__(self, *args, **kwds):
        self.counter += 1
        return self.func(*args, **kwds)


def dichotomy(a, b, eps):
    while abs(b - a) > eps:
        c = (a + b) / 2
        f1= f(c - eps)
        f2 = f(c + eps)
        if f1 < f2:
            b = c
        else:
            a = c
    print(f"local min: {round(c, 6)}")

@Counter
def f(x):
    return (1 / 2) ** x + 3 * x


def main():
    dichotomy(-2, 2, 0.000001)
    print(f"{f.func.__name__} was called {f.counter} times")


if __name__ == "__main__":
    main()