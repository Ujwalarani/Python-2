def add_numbers(a: int, b: int) -> int:
    return a + b

x: float = 5.24
y: str = "Hello, Python!"

print(add_numbers(50, 10))  # Output: 60
print(x, y)

def add_icing(func):
    def wrapper():
        print("Adding creamy icing!")
        func()
    return wrapper

def add_sprinkles(func):
    def wrapper():
        func()
        print("Tossing rainbow sprinkles!")
    return wrapper

@add_sprinkles
@add_icing
def bake_cupcake():
    print("Cupcake is baked!")

bake_cupcake()

class Car:
    def __init__(self, model: str):
        self.model = model

my_car = Car("Tesla")
print(my_car.model)  # Output: Tesla


# def fun(arg1, **kwargs):
#     for k, val in kwargs.items():
#         print("%s == %s" % (k, val))
#
#
# # Driver code
# #fun("Hi", s1='Geeks', s2='for', s3='Geeks')

def order_pizza(*toppings):
    print("You ordered a pizza with:")
    for topping in toppings:
        print(f"{topping}")

# Let's order!
order_pizza("cheese", "olives", "mushrooms")



def cupcake_order(**details):
    print("\nData type of argument:", type(details))
    print("Cupcake Order Details:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

# Place an order
cupcake_order(flavor="chocolate", frosting="vanilla", sprinkles=True, size="medium")
cupcake_order(Firstname="Sita", Lastname="Sharma", Phone=1234567890)
