word_to_morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'p': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' '
}


def word_to_morse(dict_morse):
    output = ''

    user_input = input('Enter your word: ').upper()
    for each_word in user_input:
        translate = dict_morse[each_word] + ' '
        output += translate
    return output

if __name__ == '__main__':
    print(word_to_morse(word_to_morse))
