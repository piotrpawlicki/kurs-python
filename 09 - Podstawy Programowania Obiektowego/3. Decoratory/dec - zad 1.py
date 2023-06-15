def uppercase_decorator(function):
    def make_upper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return make_upper


@uppercase_decorator
def user_input():
    return input("Enter your name: ")

print(user_input())