data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 21

data = sorted(data)
def binary_search(elem, data):
    l = 0
    p = len(data)
    while l <= p:
        s = int(( l + p ) / 2)
        if data[s] == elem:
            message = f'Odnaleziono element {elem} na liście {data}'
            return message
            break
        else:
            if data[s] < elem:
                l = s + 1
            else:
                p = s - 1
    message = f'Nie odnaleziono elementu {elem} na liście {data}'
    return message
