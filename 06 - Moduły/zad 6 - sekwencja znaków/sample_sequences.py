import random

def sample_string_only_numbers(x):

    if x == 1:
        return random.randint(0,9)
    elif x == 2:
        a = random.randint(0,9)
        return str(a) + str(a)
    else :
        numbers = [str(i) for i in range(x)]
        random.shuffle(numbers)
        index = random.randint(0, len(numbers) - 2)
        a = random.randint(0,9)
        numbers[index] = str(a)
        numbers[index+1] = numbers[index]
        random_string = ''.join(numbers)
        return random_string

def sample_string_with_user_input(number_of_strings, len_of_generated_string):
    user_input_strings = []
    for i in range(number_of_strings):
        user_input_strings.append(input("Enter a string: "))
    random_strings = []
    for i in range(len_of_generated_string):
        random_strings.append(random.choice(user_input_strings))
        generated_string =  ''.join(random_strings)
    return generated_string

def main():
    test = sample_string_with_user_input(5, 10)
    print(test)

if __name__ == "__main__":
    main()