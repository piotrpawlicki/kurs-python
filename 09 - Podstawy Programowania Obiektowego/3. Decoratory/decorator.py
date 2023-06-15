def miau_decorator(func_as_parameter):
    def miau_inside():
        print("Miau"* 10)
        func_as_parameter()
        print("Miau" * 10)

    return miau_inside

@miau_decorator
def describe_cat():
    print("Kot to najwspaniejszy przyjaciel człowieka")

@miau_decorator
def jakies_gowno():
    print("Jakies gowno")

jakies_gowno()