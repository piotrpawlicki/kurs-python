import time

def timepassed(func):
    def timer(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print("Time passed: ", end - start)
        return result
    return timer

@timepassed
def countdown(n):
    while n > 0:
        n -= 1


lista = [1000,10000,100000,1000000,100000000]
for i in lista:
    print(f'Countdown from {i}...')
    countdown(i)
    print()
