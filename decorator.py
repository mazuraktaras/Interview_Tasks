from functools import wraps


def null_decorator(func):
    def wrapper():
        print('Start working')
        print(func())
        print('Stop working')
    return wrapper


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def strong(func):
    def wrapper():
        original_result = func()
        modified_result = '<strong>' + original_result + '</strong>'
        return modified_result

    return wrapper


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() returned {original_result!r}')
        return original_result

    return wrapper

def greetings():
    return 'Hello!'

@trace
def say(name, line):
    '''Info about func'''
    return f'{name} say - {line}'


# greetings = null_decorator(greetings)
# greetings = null_decorator(greetings)
# print(greetings())
# print(say('Anna', 'Hello all!'))
print(say.__name__, say.__doc__)
