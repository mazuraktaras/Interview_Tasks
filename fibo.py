import functools
import time


def timer_logger(function):
    """
    Calculates and log the execution time of any function or method .
    :param function: Any function or method
    :return: Decorated function or method
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Get start time
        value = function(*args, **kwargs)  # Execute the function
        stop = time.perf_counter()  # Get stop time
        # Log the function name and and execution time
        # logging.info(f'EXECUTE the function {function.__name__} in {stop - start} sec.')
        print(f'Execution the function {function.__name__} in {stop - start} sec.')

        return value

    return wrapper


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoiz(memoize, n):
    if n < 2:
        return n

    if memoize[n] >= 0:
        return memoize[n]

    memoize[n] = fibonacci_memoiz(
        memoize, n - 1) + fibonacci_memoiz(memoize, n - 2)
    return memoize[n]


@timer_logger
def fibonacci_old(n):
    return fibonacci(n)


@timer_logger
def fibonacci_new(n):
    # memoize = [-1 for x in range(n + 1)]
    memoize = [-1] * (n + 1)
    return fibonacci_memoiz(memoize, n)


@timer_logger
def fibonacci_newest(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        # new_value = 3
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


print(fibonacci_old(37))
print(fibonacci_new(37))
print(fibonacci_newest(37))
