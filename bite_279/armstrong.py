def is_armstrong(n: int) -> bool:
    string_n = str(n)
    size = len(string_n)

    if size == 1:
        return True
    elif size > 1:
        total = new_func(n, size)
        return total == n


def new_func(n, size):
    return new_func1(n, size)


def new_func1(n, size):
    return sum(int(element) ** size for element in str(n))


print(is_armstrong(153))
