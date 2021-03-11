# 2. Please implement a pipe function in a language that you are good at. The
# function parameter is of indefinite length, the first parameter is a variable of
# any type, and the following parameter is the function pointer. Please attach
# unit test.

# def increment (int value) {
# return value + 1
# }
# pipe(5, increment) => 6, pipe(5, increment, increment, increment) => 8

def increment(n):
    return n+1


def pipe(n, *args):
    for i in args:
        n = i(n)
    return n


if __name__ == '__main__':
    print(pipe(5, increment))
    print(pipe(5, increment, increment, increment))
