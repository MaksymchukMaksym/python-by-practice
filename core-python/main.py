import runpy

# список модулів
MODULES = [
    "loops",
    "variables_and_types",
    "operators",
    "if_else",
    "strings",
    "functions",
    "modules"
]


def show_modules():
    print("Available modules")
    for i, names in enumerate(MODULES):
        print(f"modules {i + 1}: {names}")
    print("q. Quit")


def run_modules(module_name):
    try:
        if module_name == "modules":
            runpy.run_path(f"{module_name}.py", run_name="modules")
        else:
            runpy.run_path(f"{module_name}.py", run_name="__main__")
    except Exception as e:
        print(f"Failed to run module '{module_name}': {e}")


def main():
    while True:
        show_modules()
        choice = input("Choose module for test by number: ")
        if choice == 'q':
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(MODULES):
                run_modules(MODULES[index])
            else:
                print("Invalid number")
        except ValueError:
            print("Enter a number")


if __name__ == "__main__":
    main()
