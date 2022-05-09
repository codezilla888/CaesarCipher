import art


def coder(word: str, shift: int, status: int):
    result_word = ""
    for index, letter in enumerate(word):
        if letter in alphabet:
            current_position = alphabet.index(letter)
            new_position = (current_position + shift*status) % len(alphabet)
            result_word += alphabet[new_position]
        else:
            result_word += letter
    return result_word


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
app_working = 1
print(art.logo)
while app_working:
    coder_status = int(input("Type 1 to encrypt, type -1 to decrypt:\n"))
    word = input("Type your message:\n")
    shift = int(input("Type the shift:\n"))
    print(coder(word, shift, coder_status))
    app_working = bool(input("Type 1 if you want to go again, otherwise type 0"))




