# LEGB explanation
print("LEGB = Local → Enclosing → Global → Built-in")


# Memoization
def memoize(func):

    cache = {}

    def wrapper(*args):

        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(20))


# Fixed buggy code
total = 0


def add_to_cart(item, cart=None):
    global total

    if cart is None:
        cart = []

    cart.append(item)

    total += len(cart)

    return cart


print(add_to_cart("apple"))
print(add_to_cart("banana"))