def get_list_numbers():
    numbers = []
    while True:
        x = input("Enter a number or press 'N' to stop: ")
        try:
            if x in ('N', 'n'):
                break
            if x in ('y','Y'):
                pass
            else:
                x = int(x)
                numbers.append(x)
        except ValueError as e:
            print("Invalid number")
            with open("log.txt", "a") as f:
                f.write(f"{e} \n")
                f.close()
    return numbers

def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def main():
    numbers = get_list_numbers()
    print(average(numbers))

if __name__ == "__main__":
    main()