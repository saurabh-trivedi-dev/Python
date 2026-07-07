# Decorator : Function in a Function


import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} seconds")
#         return result
#     return wrapper

# @timer
# def example_func(n):
#     time.sleep(n)

# example_func(5)



# def debug(func):
#     def wrapper(*args, **kwargs):

#         args_values = ', '.join(str(arg) for arg in args)
#         kwargs_values = ', '.join( f"{key} = {value}" for key, value in kwargs.items())
        
#         print(f"The caller function is : {func.__name__}. The args are {args_values} and kwargs are {kwargs_values}")

#     return wrapper


# @debug
# def hello():
#     print("Hello, Kaise Hae Ji!")

# @debug
# def greet(name, greeting="Hanji"):
#     print(f"{greeting}, {name}")


# hello()
# greet("Saurabh", greeting="Hello Kaise Ho Maalik Ji")



def cache(func):

    cache_value = {}
    # print(cache_value)

    def wrapper(*args):

        if(args in cache_value):
            return cache_value[args]
        
        result = func(*args)
        cache_value[args] = result
        return result
    
    return wrapper


@cache
def long_running_func(a, b):
    time.sleep(5)
    return a+b


print(long_running_func(2, 3))
print(long_running_func(2, 3))
print(long_running_func(2, 6))