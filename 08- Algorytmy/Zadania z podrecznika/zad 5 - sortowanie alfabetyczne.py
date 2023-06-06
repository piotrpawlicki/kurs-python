data = ['5'
,'Smith'
,'Johnson'
,'Williams'
,'Brown'
,'Jones']

def delete_number(data):
    for elem in data:
        if elem.isdigit():
            data.remove(elem)
    return data


##uzyto bubble sort
def sort_data(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

data = sort_data(delete_number(data))
print(data)