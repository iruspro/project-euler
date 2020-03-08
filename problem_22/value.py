alphabetical_value = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                      'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                      'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                      'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def get_names_scores(current_name):
    points = 0
    letters = list(current_name)
    for letter in letters:
        points += alphabetical_value[letter]
    return points


def get_amount_name_scores(list_names):
    amount = 0
    current_number = 1
    for name in list_names:
        amount += current_number * get_names_scores(name)
        current_number += 1
    return amount


