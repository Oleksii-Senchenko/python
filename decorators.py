# def add(a, b):
#     return a + b
#
# operation = add
#
# print(f"Result {operation(2,4)}")


#
# def handle_get(request):
#     return "Get response"
#
# def handle_post(reusest):
#     return "Post response"
#
# routers ={
#     "Get": handle_get,
#     "Post": handle_post
# }
#
# def process_request(method, request):
#     handler = routers.get(method)
#     if handler:
#         return handler(request)
#
#     return "405 Method not allowd"
# print(process_request("Get", {}))
# print(process_request("Post", {}))
# print(process_request("Put", {}))


# def process_list(data):
#     def is_positive(x):
#         return x > 0
#     return [x for x in data if is_positive(x)]
#
# numbers = [ 5, -3,0, 10]
# print(process_list(numbers))


# def process_user_input(input_data):
#     def validate(field, value):
#         if not value:
#             raise ValueError(f"Field {field} can not be empty")
#         return value.strip()
#
#     process_data = {}
#     for field, value in input_data.items():
#         process_data[field] = validate(field, value)
#     return process_data
#
# user_data = {'username: ':"bob", 'email': 'bob@gmail.com'}
# print(process_user_input(user_data))


# def apply_opertion(a, b, operation):
#     return operation(a, b)
#
#
# def subtract(a, b):
#     return a - b
#
# print(apply_opertion(10, 4, subtract))


# def filter_records(records, criteria_func):
#     return [record for record in records if criteria_func(record)]
#
#
# def is_active_user(user):
#     return user.get("active", False)
#
#
# users = [
#     {"id": 1, "name": "Bob", "active": True},
#     {"id": 2, "name": "Alice", "active": False}
# ]
#
# active_users = filter_records(users, is_active_user)
# print(active_users)


# def greeting_factory(greeting):
#     def greet(name):
#         return f"{greeting}, {name}"
#
#     return greet
#
# say_hello = greeting_factory("Hello")
# print(say_hello("Bob"))


#с


# def rate_limited(limit):
#     calls = 0
#
#     def decorator(func):
#         # nonlocal calls
#         def wrapper(*args, **kwargs):
#             nonlocal calls
#             if calls >= limit:
#                 raise Exception("Rate limit exceeded")
#             calls += 1
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @rate_limited(limit=3)
# def api_request(endpoint):
#     return f"Responce from {endpoint}"
#
# print(api_request("/data"))
# print(api_request("/status"))
# print(api_request("/info"))
# print(api_request("/extra"))

# from time import sleep
#
# def simple_cache(func):
#     cache = {}
#
#     def wrapper(*args):
#         nonlocal cache
#         if args in cache:
#             print("[CACHE] возврощаем кэшированый результат")
#             return cache[args]
#
#         result = func(*args)
#         cache[args] = result
#         return result
#
#     return wrapper
#
# @simple_cache
# def slow_func(x):
#     print("Обчисливаетсья результат")
#     print(x + x)
#
# @simple_cache
# def slow_func2(x):
#     for i in range(1,5):
#         print("Sleep")
#         sleep(1)
#     return 2*x
#
#
#
# print("Result", slow_func2(100))
# print("Result", slow_func2(1000))
# print("Result", slow_func2(100))
# print("Result", slow_func2(1000))
# print("Result", slow_func2(10))
# print("Result", slow_func(4))
# print("Result", slow_func(4))
# print("Result", slow_func(5))
# print("Result", slow_func(5))

def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            raise PermissionError("Only for admins..")
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def delete_user(user, user_id):
    return f"User {user_id} delete"

admin = {"name": "Alisa", "role": "admin"}
regular_user = {"name": "Bob", "role":"user"}

print(f"Delete {delete_user(admin, 42)}")

try:
    print(f"Delete {delete_user(regular_user, 42)}")
except PermissionError as e:
    print(f"Access denied: {e}")

# print(f"Delete {delete_user(admin, 42)}")
# print(f"Delete {delete_user(regular_user, 41)}")

# import time
#
# def ttl_cache(ttl):
#     cache = {}
#     def decorator(func):
#         nonlocal cache
#         def wrapper(*args, **kwargs):
#             nonlocal cache
#             key = (args, frozenset(kwargs.items()))
#
#             current_time = time.time()
#             if key in cache:
#                 result, timestamp = cache[key]
#                 if current_time - timestamp < ttl:
#                     print("[CACHE]")
#                     return result
#             result = func(*args, **kwargs)
#             cache[key] = (result, current_time)
#             return result
#         return wrapper
#     return decorator
#
#
# @ttl_cache(ttl=5)
# def get_data(x):
#     print("Result...")
#     return x * 10
# print(f"Result: {get_data(3)}")
# time.sleep(3)
# print(f"Result: {get_data(3)}")
# time.sleep(3)
# print(f"Result: {get_data(3)}")


# def error_handler_factory(logger):
#     def error_handler(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args,**kwargs)
#             except Exception as e:
#                 logger.error(f"Error in {func.__name__}: {e}")
#                 return None
#         return wrapper
#     return error_handler
#
# class SimpleLogger:
#     def error(self, message):
#         print(f'[ERROR] {message}')
#
# logger = SimpleLogger()
# handel_error = error_handler_factory(logger)

# @handel_error
# def procces_order(order):
#     if order.get('ammount', 0) <= 0:
#         raise ValueError("Amount <= 0")
#     return "Order processed"
#
# print(procces_order({"amount": 10}))
# print(procces_order({"amount": -5}))
#





def process_order1(order):
    if order.get('amount', 0) <= 0:
        raise ValueError("Amount <= 0")
    return "Order processed"
try:
    result = process_order1({"amount": 10})
    print(result)
    result2 = process_order1({"amount": -2})
    print(result2)
except Exception as e:
    print(f"[ERROR] {e}")


# --------------------------



def error(message):
    print(f'[ERROR] {message}')

def error_handler_factory(func_error):
    def error_handler(func):
        def wrapper(order):
            try:
                return func(order)
            except Exception as e:
                func_error(f"Error in {func.__name__}: {e}")
        return wrapper
    return error_handler

handle_error = error_handler_factory(error)

@handle_error
def process_order(order):
    if order.get("amount", 0) <= 0:
        raise ValueError("Amount <= 0")
    return "Order processed"

print(process_order({"amount": 10}))
print(process_order({"amount": -5}))