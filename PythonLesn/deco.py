def print_result(f):
    def result(x):
        r = f(x)
        print(f'Результат вычисления: {r}')
        return r

    return result


@print_result
def triple(x):
    return x * 3


@print_result
def divide(x):
    return x / 5


triple(5)
divide(5)
