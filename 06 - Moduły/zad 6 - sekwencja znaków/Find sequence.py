# Given a string, find the longest sequence of characters that are the same.
# Example:var ='banannnnannnnnnnnnanananananaaaana'
import sample_sequences as sseq
def find_sequence(testing_string):
    sequence = ''
    sequence_temp = ''
    for each in testing_string:
        if each == sequence_temp[-1:]:
            sequence_temp += each
        else:
            sequence_temp = each
        if len(sequence_temp) > len(sequence):
            sequence = sequence_temp
    return sequence
def main():
    number_of_strings = int(input('Enter the number of chars: '))
    len_of_generated_string = int(input('Enter the length of generated string to test: '))
    var = sseq.sample_string_with_user_input(number_of_strings,len_of_generated_string)
    print(f'String to test is : {var}')
    sequence = find_sequence(var)
    print(sequence)
    print(len(sequence))


if __name__ == '__main__':
    main()