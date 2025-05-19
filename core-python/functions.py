import inspect


# sum
def task_1(a, b):
    return a + b


def get_arguments_for_function(func):
    sig = inspect.signature(func)

    args = []
    for param in sig.parameters.values():
        val = input(f"Enter value for {param.name} ({param.kind}): ")
        args.append(eval(val))
    return args


if __name__ == "__main__":
    while True:
        n = input("change number of task: ")
        print("q. Quit")
        if n != 'q':
            func = globals().get(f"task_{n}")
            if func is None:
                print("No such function.")
                continue
            args = get_arguments_for_function(func)
            result = func(*args)
            if result is not None:
                print("Result:", result)
        else:
            break
