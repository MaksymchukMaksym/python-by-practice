import inspect


# sum
def task_1(a, b):
    return a + b


# count_even_odd
def task_2(lst):
    even = len([n for n in lst if n % 2 == 0])
    odd = len([n for n in lst if n % 2 != 0])
    return even, odd


# get_max_min_avg
def task_3(lst):
    return min(lst), max(lst), sum(lst) / len(lst)


# apply_operation
def task_4(a, b, operation):
    return operation(a, b)


# factorial_recursive
def task_5(n):
    if n == 0 or n == 1:
        return 1
    return n * task_5(n - 1)


# greet_all
def task_6(*args):
    for el in args:
        print(f"Greating for: {el}")


# build_user
def task_7(**kwargs):
    return dict(kwargs)


def get_arguments_for_function(func):
    sig = inspect.signature(func)

    args = []
    kwargs = {}
    for param in sig.parameters.values():
        if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            choice = input(f"Do you want to pass '{param.name}' as keyword? (y/n): ")
            val = input(f"Enter value for {param.name}: ")
            if choice == "y":
                kwargs[param.name] = eval(val)
            else:
                args.append(eval(val))

        if param.kind == inspect.Parameter.VAR_POSITIONAL:
            val = input(f"Enter sequence of value for {param.name}: ")
            args.extend(tuple(eval(el) for el in val.split()))

        if param.kind == inspect.Parameter.VAR_KEYWORD:
            val = input("Enter dict-like string for keyword args (e.g. {'a':1, 'b':2}): ")
            kwargs.update(eval(val))

    return args, kwargs


if __name__ == "__main__":
    while True:
        n = input("change number of task: ")
        print("q. Quit")
        if n != 'q':
            func = globals().get(f"task_{n}")
            if func is None:
                print("No such function.")
                continue
            args, kwargs = get_arguments_for_function(func)
            result = func(*args, **kwargs)
            if result is not None:
                print("Result:", result)
        else:
            break
