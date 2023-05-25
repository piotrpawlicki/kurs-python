print('Jestem w pliku test')

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


def find_longest_word(sequences):
    longest = ''
    for word in sequences:
        if len(word) > len(longest):
            longest = word
    return longest

def find_shortest_word(sequences):
    shortest = ''
    for word in sequences:
        if len(word) < len(shortest):
            shortest = word
    return shortest
