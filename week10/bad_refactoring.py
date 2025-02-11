"""
Make this a function:
Input values: num_for_loops, lines, filename
Output value: num_while_loops
(NB: "Output" doesn't mean "stuff we print")
"""

def get_file():
    """
    Get a file function. Asks a file name, opens it and returns a file object.
    :return: a file object
    """
    file_name = input("Enter program filename: ")
    return open(file_name)

def print_file_containing(file):
    lines = file.readlines()
    print_output(file, get_num_for_loops(lines))
    print_output(file, get_num_while_loops(lines))
    print_output(file, get_num_if_loops(lines))

def get_num_for_loops(lines):
    result = 0
    for line in lines:
        if line.strip().startswith("for"):
            result += 1
    return result

def get_num_while_loops(lines):
    result = 0
    for line in lines:
        if line.strip().startswith("while"):
            result += 1
    return result

def get_num_if_loops(lines):
    result = 0
    for line in lines:
        if line.strip().startswith("if"):
            result += 1
    return result

def print_output(file, value):
    print("Program {} contain {} for loops".format(file.name, value))

def main():
    """
    Main function. Read file. Count required attributes
    :return:
    """

    file = get_file()
    # function prints the number of occurrences of the following words: for; while; if
    print_file_containing(file)

if __name__ == '__main__':
    main()
