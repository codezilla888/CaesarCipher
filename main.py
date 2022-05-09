def coder(word: str, shift: int, status: int):
    result_word = ""
    for index, letter in enumerate(word):
        current_position = alphabet.index(letter)
        new_position = (current_position + shift*status) % len(alphabet)
        result_word += alphabet[new_position]
    return result_word


coder_status = int(input("Type 1 to encrypt, type -1 to decrypt:\n"))
word = input("Type your message:\n")
shift = int(input("Type the shift:\n"))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

print(coder(word, shift, coder_status))

